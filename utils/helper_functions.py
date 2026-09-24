"""
Helper / utility functions for the Vigyan Shaala Attendance app.
"""

from datetime import datetime, timezone, timedelta


# Indian Standard Time offset
_IST = timezone(timedelta(hours=5, minutes=30))


def get_ist_timestamp() -> str:
    """Return the current timestamp in IST as a formatted string."""
    return datetime.now(_IST).strftime("%Y-%m-%d %H:%M:%S IST")


def validate_attendance(
    attendance_map: dict[str, str],
    student_names: list[str],
) -> tuple[bool, str]:
    """
    Validate that every student has been marked Present or Absent.

    Parameters
    ----------
    attendance_map : dict
        Mapping of student name → "Present" / "Absent" / None.
    student_names : list
        All student names expected in the submission.

    Returns
    -------
    (is_valid, error_message)
    """
    unmarked = [
        name for name in student_names
        if attendance_map.get(name) not in ("Present", "Absent")
    ]
    if unmarked:
        return False, f"Please mark attendance for: {', '.join(unmarked)}"
    return True, ""
