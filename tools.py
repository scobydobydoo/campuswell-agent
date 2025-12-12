def parse_student_profile(profile: str) -> dict:
    return {"raw_profile": profile}

def make_email_template(name: str, course: str) -> dict:
    return {
        "template": f"Hello Professor,\n\nI am {name} from {course}. I would like to request your guidance.\n\nRegards,\n{name}"
    }

def save_plan_to_file(plan_text: str, filename: str) -> dict:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(plan_text)
    return {"status": "saved", "filename": filename}
