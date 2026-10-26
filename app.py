import streamlit as st

from study_agent import (
    generate_study_plan,
    get_next_task,
    get_progress,
)

st.set_page_config(
    page_title="AI Study Planner Agent",
    page_icon="📚",
    layout="wide",
)

# Initialize session data.
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "next_id" not in st.session_state:
    st.session_state.next_id = 1

if "show_plan" not in st.session_state:
    st.session_state.show_plan = False

st.title("📚 AI Study Planner Agent")
st.write(
    "Plan your studies according to difficulty, "
    "deadlines, and available time."
)

# Sidebar settings.
st.sidebar.header("Study Settings")

daily_hours = st.sidebar.slider(
    "Available study hours per day",
    min_value=1,
    max_value=12,
    value=4,
)

# Add a topic.
st.subheader("Add a Study Topic")

with st.form("add_task_form", clear_on_submit=True):
    subject = st.text_input(
        "Subject",
        placeholder="e.g. Machine Learning",
    )

    topic = st.text_input(
        "Topic",
        placeholder="e.g. Decision Trees",
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"],
        )

    with col2:
        deadline_days = st.number_input(
            "Days until deadline",
            min_value=0,
            max_value=365,
            value=3,
            step=1,
        )

    with col3:
        study_hours = st.number_input(
            "Estimated study hours",
            min_value=0.5,
            max_value=100.0,
            value=1.0,
            step=0.5,
        )

    submitted = st.form_submit_button(
        "Add Topic",
        type="primary",
        use_container_width=True,
    )

    if submitted:
        if subject.strip() and topic.strip():
            st.session_state.tasks.append({
                "id": st.session_state.next_id,
                "subject": subject.strip(),
                "topic": topic.strip(),
                "difficulty": difficulty,
                "deadline_days": int(deadline_days),
                "remaining_hours": float(study_hours),
                "completed": False,
            })

            st.session_state.next_id += 1
            st.session_state.show_plan = False

            st.rerun()
        else:
            st.error("Enter both a subject and a topic.")

tasks = st.session_state.tasks

# Dashboard.
st.divider()
st.subheader("Your Study Dashboard")

total = len(tasks)
completed = sum(task["completed"] for task in tasks)
pending = total - completed
progress = get_progress(tasks)

col1, col2, col3 = st.columns(3)

col1.metric("Total Topics", total)
col2.metric("Pending Topics", pending)
col3.metric("Completed Topics", completed)

st.progress(progress / 100)
st.caption(f"Overall completion: {progress}%")

# Generate the schedule.
st.divider()
st.subheader("Today's Study Plan")

if st.button("Generate / Re-plan My Day", type="primary"):
    st.session_state.show_plan = True

if st.session_state.show_plan:
    plan = generate_study_plan(tasks, daily_hours)
    next_task = get_next_task(plan)

    if next_task:
        st.success(
            f"Recommended next: {next_task['subject']} — "
            f"{next_task['topic']}"
        )

        for index, item in enumerate(plan, start=1):
            with st.container(border=True):
                st.markdown(
                    f"**{index}. {item['subject']} — "
                    f"{item['topic']}**"
                )

                st.write(
                    f"Allocated time: {item['hours']} hour(s)"
                )

                st.caption(
                    f"Priority score: {item['priority']}"
                )

        allocated = sum(item["hours"] for item in plan)

        st.info(
            f"Scheduled {allocated:g} out of "
            f"{daily_hours} available hours."
        )
    elif tasks:
        st.success("All topics are completed!")
    else:
        st.info("Add topics before generating your plan.")

# Manage topics.
st.divider()
st.subheader("Manage Your Topics")

if not tasks:
    st.write("Your topic list is empty.")
else:
    for task in tasks:
        with st.container(border=True):
            left, right = st.columns([4, 1])

            with left:
                st.markdown(
                    f"**{task['subject']} — {task['topic']}**"
                )

                st.caption(
                    f"Difficulty: {task['difficulty']} | "
                    f"Deadline: {task['deadline_days']} day(s) | "
                    f"Estimated remaining time: "
                    f"{task['remaining_hours']:g} hour(s)"
                )

            with right:
                if task["completed"]:
                    st.success("Completed")
                elif st.button(
                    "Complete",
                    key=f"complete_{task['id']}",
                    use_container_width=True,
                ):
                    task["completed"] = True
                    task["remaining_hours"] = 0
                    st.session_state.show_plan = True
                    st.rerun()

    if st.button("Clear All Topics"):
        st.session_state.tasks = []
        st.session_state.show_plan = False
        st.rerun()

st.divider()

st.caption(
    "AI Study Planner Agent | Python + Streamlit | "

)
