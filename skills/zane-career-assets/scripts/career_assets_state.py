#!/usr/bin/env python3
"""Maintain review gates, decisions, and per-artifact states for career assets."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

GATES = (
    "task_contract",
    "evidence_position",
    "content",
    "structure",
    "visual",
    "qa",
    "final_confirmation",
)
STATUSES = ("pending", "checked", "approved", "waived", "not_required")
DECISION_STATUSES = ("proposal", "recommended", "confirmed", "rejected", "constraint", "open")
DECISION_AREAS = ("task", "fact", "position", "content", "structure", "visual", "language", "release")
ARTIFACT_STATUSES = (
    "draft",
    "candidate",
    "confirmed",
    "release_ready",
    "deployed",
    "real_world_validated",
    "on_hold",
    "not_required",
    "rejected",
)
PROJECT_PHASES = ("intake", "modeling", "production", "qa", "release", "feedback", "complete")
CONTRACT_NAMES = (
    "task",
    "market",
    "privacy",
    "evidence",
    "claims",
    "carrier",
    "terminology",
    "structure",
    "visual",
    "validation",
    "release",
)
CONTRACT_STATUSES = ("missing", "draft", "current", "frozen")
ACTION_REQUIREMENTS = {
    "build-resume": ("task_contract", "evidence_position", "content", "structure", "visual"),
    "build-website": ("task_contract", "evidence_position", "content", "structure", "visual"),
    "release": GATES,
}


def load_state(path: Path) -> dict:
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"state file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in state file: {path}: {exc}") from exc
    if state.get("schema_version") not in {1, 2, 3} or not isinstance(state.get("gates"), dict):
        raise SystemExit("unsupported or incomplete zane-career-assets state")
    state.setdefault("decisions", [])
    state.setdefault("artifacts", {})
    state.setdefault("contracts", {})
    state.setdefault("project_phase", "legacy")
    state.setdefault("excluded_inputs", [])
    # Preserve legacy fields/history. Old implicit gates were not an explicit
    # request to pause. Global approvals cannot certify multiple artifacts.
    legacy = state.get("schema_version") in {1, 2}
    state.setdefault("review_mode", "deliver")
    state.setdefault("pause_at", [])
    if not state["artifacts"] and len(state.get("scope", [])) == 1:
        state["artifacts"][state["scope"][0]] = {"status": state.get("artifact_status", "draft")}
    for item in state["artifacts"].values():
        item.setdefault("gates", deepcopy(state["gates"]) if legacy and len(state["artifacts"]) == 1 else {})
        item.setdefault("validity", "current")
        item.setdefault("history", [])
    state["schema_version"] = 3
    return state


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def artifact_for(state: dict, name: str) -> tuple[str, dict]:
    if not name:
        if len(state["artifacts"]) != 1:
            raise SystemExit("--artifact is required when the project has multiple or no artifacts")
        name = next(iter(state["artifacts"]))
    if name not in state["artifacts"]:
        raise SystemExit(f"unknown artifact: {name}")
    return name, state["artifacts"][name]


def release_missing(item: dict) -> list[str]:
    missing = []
    if item.get("validity") != "current":
        missing.append("current version needs review")
    for gate, allowed in (("qa", {"checked", "approved"}), ("final_confirmation", {"approved"})):
        value = item.get("gates", {}).get(gate, {})
        if value.get("status") not in allowed or not value.get("note", "").strip():
            missing.append(gate)
        if gate == "qa" and not value.get("evidence", "").strip():
            missing.append("qa evidence")
    return missing


def write_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def command_init(args: argparse.Namespace) -> None:
    path = Path(args.state)
    if path.exists() and not args.force:
        raise SystemExit(f"state file already exists: {path}; use --force only for an intentional restart")
    if path.exists():
        backup = path.with_name(path.name + ".backup-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ"))
        shutil.copy2(path, backup)
        print(f"previous state preserved: {backup}")
    state = {
        "schema_version": 3,
        "review_mode": "deliver",
        "pause_at": [],
        "project": args.project,
        "scope": [item.strip() for item in args.scope.split(",") if item.strip()],
        "project_phase": "intake",
        "artifacts": {
            item: {"status": "draft", "source": "", "destination": "", "updated_at": "", "validity": "current", "gates": {}, "history": []}
            for item in [part.strip() for part in args.scope.split(",") if part.strip()]
        },
        "contracts": {
            name: {"status": "missing", "path": "", "updated_at": ""} for name in CONTRACT_NAMES
        },
        "decisions": [],
        "excluded_inputs": [],
        "gates": {
            gate: {"status": "pending", "note": "", "evidence": "", "decided_at": ""}
            for gate in GATES
        },
    }
    write_state(path, state)
    print(f"initialized: {path}")


def command_mode(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    selected = [x.strip() for x in args.pause_at.split(",") if x.strip()]
    if any(x not in GATES[:5] for x in selected):
        raise SystemExit("pause-at accepts only intermediate production gates")
    if args.review_mode == "staged" and not selected:
        raise SystemExit("staged mode needs the user's actual --pause-at checkpoints")
    if not args.note.strip():
        raise SystemExit("--note must record the user's chosen review mode")
    state.update(review_mode=args.review_mode, pause_at=selected if args.review_mode == "staged" else [])
    state.setdefault("mode_history", []).append({"mode": state["review_mode"], "pause_at": state["pause_at"], "note": args.note, "at": now()})
    write_state(state_path, state)


def command_decide(args: argparse.Namespace) -> None:
    if not args.note.strip():
        raise SystemExit("--note must explain the check or user decision")
    state_path = Path(args.state)
    state = load_state(state_path)
    if args.gate in {"qa", "final_confirmation"} or args.artifact:
        _, item = artifact_for(state, args.artifact)
        if item["validity"] != "current":
            raise SystemExit("record an updated candidate before checking or confirming a stale artifact")
        gates = item.setdefault("gates", {})
    else:
        gates = state["gates"]
    gates[args.gate] = {"status": args.status, "note": args.note.strip(), "evidence": args.evidence.strip(), "decided_at": now()}
    write_state(state_path, state)
    print(f"recorded: {args.gate}={args.status}")


def command_reopen(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    start = GATES.index(args.gate)
    selected = [x.strip() for x in args.affects.split(",") if x.strip()] or list(state["artifacts"])
    for name in selected:
        artifact_for(state, name)
    if not args.note.strip():
        raise SystemExit("--note must explain what changed")
    for name in selected:
        item = state["artifacts"][name]
        item.setdefault("history", []).append({"status": item.get("status"), "source": item.get("source"), "destination": item.get("destination"), "gates": deepcopy(item.get("gates", {})), "at": now(), "reason": args.note})
        # Deployed is a historical fact; validity marks whether current use is safe.
        item["validity"] = "needs_review"
        for gate in GATES[start:]:
            item.setdefault("gates", {})[gate] = {"status": "pending", "note": "", "evidence": ""}
    # A targeted reopen does not erase unrelated artifact approvals.
    if not args.affects:
        for gate in GATES[start:]:
            state["gates"][gate] = {"status": "pending", "note": "", "evidence": ""}
    state.setdefault("changes", []).append({"gate": args.gate, "affects": selected, "note": args.note, "at": now()})
    write_state(state_path, state)
    print(f"reopened: {', '.join(selected)}")


def command_record(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    statement = args.statement.strip()
    reason = args.reason.strip()
    if not statement or not reason:
        raise SystemExit("--statement and --reason are required")
    next_id = max((item.get("id", 0) for item in state["decisions"]), default=0) + 1
    state["decisions"].append(
        {
            "id": next_id,
            "area": args.area,
            "status": args.status,
            "statement": statement,
            "reason": reason,
            "affects": [item.strip() for item in args.affects.split(",") if item.strip()],
            "recorded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
    )
    write_state(state_path, state)
    print(f"recorded decision: {next_id} {args.area}/{args.status}")


def command_artifact(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    current = state["artifacts"].setdefault(args.name, {"gates": {}, "validity": "current", "history": []})
    if args.status in {"confirmed", "release_ready", "deployed", "real_world_validated"}:
        missing = release_missing(current)
        if args.source.strip() and args.source.strip() != current.get("source", ""):
            missing.append("changed source must be recorded as a candidate first")
        if missing:
            raise SystemExit("cannot promote artifact: " + ", ".join(missing))
    if args.status in {"draft", "candidate"}:
        if not args.source.strip() and current.get("validity") == "needs_review":
            raise SystemExit("updated candidate requires --source")
        if current.get("status"):
            current.setdefault("history", []).append({"status": current.get("status"), "source": current.get("source"), "destination": current.get("destination"), "gates": deepcopy(current.get("gates", {})), "at": now()})
        current["gates"] = {}
        current["validity"] = "current"
    current.update(status=args.status, source=args.source.strip() or current.get("source", ""), destination=args.destination.strip() or current.get("destination", ""), updated_at=now())
    write_state(state_path, state)
    print(f"recorded artifact: {args.name}={args.status}")


def command_contract(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    contracts = state.setdefault("contracts", {})
    contracts[args.name] = {
        "status": args.status,
        "path": args.path.strip(),
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    write_state(state_path, state)
    print(f"recorded contract: {args.name}={args.status}")


def command_phase(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    state["project_phase"] = args.phase
    write_state(state_path, state)
    print(f"recorded project phase: {args.phase}")


def command_exclude(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    state.setdefault("excluded_inputs", []).append(
        {
            "description": args.description.strip(),
            "reason": args.reason.strip(),
            "replacement": args.replacement.strip(),
            "recorded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
    )
    write_state(state_path, state)
    print("recorded excluded input")


def command_check(args: argparse.Namespace) -> None:
    state = load_state(Path(args.state))
    missing = []
    if args.action == "release":
        _, item = artifact_for(state, args.artifact)
        missing = release_missing(item)
    elif state["review_mode"] == "staged":
        gates = dict(state["gates"])
        if args.artifact:
            _, item = artifact_for(state, args.artifact)
            gates.update(item.get("gates", {}))
        for gate in state["pause_at"]:
            value = gates.get(gate, {})
            if value.get("status") not in {"approved", "waived", "not_required"} or not value.get("note", "").strip():
                missing.append(gate)
    if missing:
        print(f"BLOCKED {args.action}: {', '.join(missing)}")
        raise SystemExit(2)
    print(f"PASS {args.action}" + (" (candidate production only)" if args.action != "release" else " (recorded QA and user confirmation; external authorization is separate)"))


def command_show(args: argparse.Namespace) -> None:
    state = load_state(Path(args.state))
    print(f"project: {state.get('project', '')}")
    print(f"scope: {', '.join(state.get('scope', []))}")
    print(f"review_mode: {state['review_mode']} | pause_at: {state['pause_at']}")
    print(f"project_phase: {state.get('project_phase', 'legacy')}")
    if "artifact_status" in state:
        print(f"legacy_artifact_status: {state.get('artifact_status', '')}")
    for gate in GATES:
        item = state["gates"].get(gate, {})
        print(f"{gate}: {item.get('status', 'missing')} | {item.get('note', '')}")
    for name, item in state.get("artifacts", {}).items():
        print(f"artifact {name}: {item.get('status', 'missing')} | {item.get('destination', '')}")
    for name, item in state.get("contracts", {}).items():
        print(f"contract {name}: {item.get('status', 'missing')} | {item.get('path', '')}")
    print(f"decisions: {len(state.get('decisions', []))}")
    print(f"excluded_inputs: {len(state.get('excluded_inputs', []))}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("--state", required=True)
    init.add_argument("--project", required=True)
    init.add_argument("--scope", required=True, help="comma-separated deliverable scopes")
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=command_init)

    decide = sub.add_parser("decide")
    decide.add_argument("--state", required=True)
    decide.add_argument("--artifact", default="")
    decide.add_argument("--gate", required=True, choices=GATES)
    decide.add_argument("--status", required=True, choices=STATUSES[1:])
    decide.add_argument("--note", required=True)
    decide.add_argument("--evidence", default="", help="path or identifier of the reviewed artifact")
    decide.set_defaults(func=command_decide)

    reopen = sub.add_parser("reopen")
    reopen.add_argument("--state", required=True)
    reopen.add_argument("--gate", required=True, choices=GATES)
    reopen.add_argument("--affects", default="")
    reopen.add_argument("--note", required=True)
    reopen.set_defaults(func=command_reopen)

    record = sub.add_parser("record")
    record.add_argument("--state", required=True)
    record.add_argument("--area", required=True, choices=DECISION_AREAS)
    record.add_argument("--status", required=True, choices=DECISION_STATUSES)
    record.add_argument("--statement", required=True)
    record.add_argument("--reason", required=True)
    record.add_argument("--affects", default="", help="comma-separated affected artifacts or layers")
    record.set_defaults(func=command_record)

    artifact = sub.add_parser("artifact")
    artifact.add_argument("--state", required=True)
    artifact.add_argument("--name", required=True)
    artifact.add_argument("--status", required=True, choices=ARTIFACT_STATUSES)
    artifact.add_argument("--source", default="")
    artifact.add_argument("--destination", default="")
    artifact.set_defaults(func=command_artifact)

    contract = sub.add_parser("contract")
    contract.add_argument("--state", required=True)
    contract.add_argument("--name", required=True, choices=CONTRACT_NAMES)
    contract.add_argument("--status", required=True, choices=CONTRACT_STATUSES)
    contract.add_argument("--path", default="")
    contract.set_defaults(func=command_contract)

    phase = sub.add_parser("phase")
    phase.add_argument("--state", required=True)
    phase.add_argument("--phase", required=True, choices=PROJECT_PHASES)
    phase.set_defaults(func=command_phase)

    exclude = sub.add_parser("exclude")
    exclude.add_argument("--state", required=True)
    exclude.add_argument("--description", required=True, help="descriptor only; do not copy sensitive content")
    exclude.add_argument("--reason", required=True)
    exclude.add_argument("--replacement", default="", help="redacted summary or safer evidence to request")
    exclude.set_defaults(func=command_exclude)

    check = sub.add_parser("check")
    check.add_argument("--state", required=True)
    check.add_argument("--action", required=True, choices=tuple(ACTION_REQUIREMENTS))
    check.add_argument("--artifact", default="")
    check.set_defaults(func=command_check)

    mode = sub.add_parser("mode")
    mode.add_argument("--state", required=True)
    mode.add_argument("--review-mode", required=True, choices=("deliver", "staged"))
    mode.add_argument("--pause-at", default="")
    mode.add_argument("--note", required=True)
    mode.set_defaults(func=command_mode)

    show = sub.add_parser("show")
    show.add_argument("--state", required=True)
    show.set_defaults(func=command_show)
    return parser


if __name__ == "__main__":
    parsed = build_parser().parse_args()
    parsed.func(parsed)
