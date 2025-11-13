import streamlit as st
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import date, datetime
import json

# Load environment variables
load_dotenv()

# Initialize Supabase client - check both env vars and Streamlit secrets
SUPABASE_URL = os.getenv("SUPABASE_URL") or st.secrets.get("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY") or st.secrets.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("Please set SUPABASE_URL and SUPABASE_KEY in your .env file or Streamlit secrets")
    st.info("For local development: Create a .env file with your Supabase credentials")
    st.info("For Streamlit Cloud: Add credentials in the app settings under 'Secrets'")
    st.stop()

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Configure page
st.set_page_config(
    page_title="Personal Trainer App",
    page_icon="💪",
    layout="wide"
)

# Session state initialization
if 'user' not in st.session_state:
    st.session_state.user = None
if 'profile' not in st.session_state:
    st.session_state.profile = None

# Authentication functions
def sign_up(email, password, full_name, role):
    """Sign up a new user"""
    try:
        # Create user in Supabase Auth
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "data": {
                    "full_name": full_name,
                    "role": role
                }
            }
        })
        
        if response.user:
            # If email confirmation is enabled, user needs to verify email
            if not response.session:
                return True, "Account created! Please check your email and click the confirmation link to complete setup."
            
            # If no email confirmation required, update profile directly
            supabase.table('profiles').update({
                'full_name': full_name,
                'role': role
            }).eq('id', response.user.id).execute()
            
            return True, "Account created successfully!"
        return False, "Failed to create account"
    except Exception as e:
        error_msg = str(e)
        if "Invalid API key" in error_msg:
            return False, "Authentication configuration error. Please check Supabase settings."
        return False, f"Error creating account: {error_msg}"

def sign_in(email, password):
    """Sign in an existing user"""
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        
        if response.user:
            st.session_state.user = response.user
            # Fetch user profile
            profile_response = supabase.table('profiles').select('*').eq('id', response.user.id).execute()
            if profile_response.data:
                st.session_state.profile = profile_response.data[0]
            return True, "Logged in successfully!"
        return False, "Invalid credentials"
    except Exception as e:
        return False, str(e)

def sign_out():
    """Sign out the current user"""
    try:
        supabase.auth.sign_out()
        st.session_state.user = None
        st.session_state.profile = None
        return True
    except Exception as e:
        st.error(f"Error signing out: {e}")
        return False

# Workout functions
def create_workout(title, description, exercises):
    """Create a new workout"""
    try:
        data = {
            'trainer_id': st.session_state.user.id,
            'title': title,
            'description': description,
            'exercises': exercises
        }
        response = supabase.table('workouts').insert(data).execute()
        return True, "Workout created successfully!"
    except Exception as e:
        return False, str(e)

def get_workouts():
    """Get all workouts for the current trainer"""
    try:
        response = supabase.table('workouts').select('*').eq('trainer_id', st.session_state.user.id).execute()
        return response.data
    except Exception as e:
        st.error(f"Error fetching workouts: {e}")
        return []

def delete_workout(workout_id):
    """Delete a workout"""
    try:
        supabase.table('workouts').delete().eq('id', workout_id).execute()
        return True, "Workout deleted successfully!"
    except Exception as e:
        return False, str(e)

# Meal plan functions
def create_meal_plan(title, description, meals):
    """Create a new meal plan"""
    try:
        data = {
            'trainer_id': st.session_state.user.id,
            'title': title,
            'description': description,
            'meals': meals
        }
        response = supabase.table('meal_plans').insert(data).execute()
        return True, "Meal plan created successfully!"
    except Exception as e:
        return False, str(e)

def get_meal_plans():
    """Get all meal plans for the current trainer"""
    try:
        response = supabase.table('meal_plans').select('*').eq('trainer_id', st.session_state.user.id).execute()
        return response.data
    except Exception as e:
        st.error(f"Error fetching meal plans: {e}")
        return []

def delete_meal_plan(meal_plan_id):
    """Delete a meal plan"""
    try:
        supabase.table('meal_plans').delete().eq('id', meal_plan_id).execute()
        return True, "Meal plan deleted successfully!"
    except Exception as e:
        return False, str(e)

# Client functions
def get_clients():
    """Get all clients"""
    try:
        response = supabase.table('profiles').select('*').eq('role', 'client').execute()
        return response.data
    except Exception as e:
        st.error(f"Error fetching clients: {e}")
        return []

# Assignment functions
def assign_workout(workout_id, client_id, assigned_date):
    """Assign a workout to a client"""
    try:
        data = {
            'workout_id': workout_id,
            'client_id': client_id,
            'assigned_date': assigned_date.isoformat()
        }
        response = supabase.table('workout_assignments').insert(data).execute()
        return True, "Workout assigned successfully!"
    except Exception as e:
        return False, str(e)

def assign_meal_plan(meal_plan_id, client_id, assigned_date):
    """Assign a meal plan to a client"""
    try:
        data = {
            'meal_plan_id': meal_plan_id,
            'client_id': client_id,
            'assigned_date': assigned_date.isoformat()
        }
        response = supabase.table('meal_assignments').insert(data).execute()
        return True, "Meal plan assigned successfully!"
    except Exception as e:
        return False, str(e)

def get_today_assignments():
    """Get today's assignments for the current client"""
    try:
        today = date.today().isoformat()
        
        # Get workout assignments
        workout_response = supabase.table('workout_assignments').select(
            '*, workouts(*)'
        ).eq('client_id', st.session_state.user.id).eq('assigned_date', today).execute()
        
        # Get meal assignments
        meal_response = supabase.table('meal_assignments').select(
            '*, meal_plans(*)'
        ).eq('client_id', st.session_state.user.id).eq('assigned_date', today).execute()
        
        return workout_response.data, meal_response.data
    except Exception as e:
        st.error(f"Error fetching today's assignments: {e}")
        return [], []

def mark_workout_complete(assignment_id, completed):
    """Mark a workout assignment as complete or incomplete"""
    try:
        data = {
            'completed': completed,
            'completed_at': datetime.now().isoformat() if completed else None
        }
        supabase.table('workout_assignments').update(data).eq('id', assignment_id).execute()
        return True
    except Exception as e:
        st.error(f"Error updating workout: {e}")
        return False

def mark_meal_complete(assignment_id, completed):
    """Mark a meal assignment as complete or incomplete"""
    try:
        data = {
            'completed': completed,
            'completed_at': datetime.now().isoformat() if completed else None
        }
        supabase.table('meal_assignments').update(data).eq('id', assignment_id).execute()
        return True
    except Exception as e:
        st.error(f"Error updating meal: {e}")
        return False

# UI Pages
def login_page():
    """Display login/signup page"""
    st.title("💪 Personal Trainer App")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        st.subheader("Login")
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
                if email and password:
                    success, message = sign_in(email, password)
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.error("Please fill in all fields")
    
    with tab2:
        st.subheader("Create Account")
        with st.form("signup_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            full_name = st.text_input("Full Name")
            role = st.selectbox("I am a:", ["client", "trainer"])
            submit = st.form_submit_button("Sign Up")
            
            if submit:
                if email and password and full_name:
                    success, message = sign_up(email, password, full_name, role)
                    if success:
                        st.success(message)
                    else:
                        st.error(message)
                else:
                    st.error("Please fill in all fields")

def trainer_dashboard():
    """Display trainer dashboard"""
    st.title(f"👋 Welcome, {st.session_state.profile.get('full_name', 'Trainer')}")
    
    if st.sidebar.button("Logout"):
        sign_out()
        st.rerun()
    
    # Navigation
    page = st.sidebar.radio("Navigation", ["Workouts", "Meal Plans", "Assign to Clients"])
    
    if page == "Workouts":
        workout_management_page()
    elif page == "Meal Plans":
        meal_plan_management_page()
    elif page == "Assign to Clients":
        assignment_page()

def workout_management_page():
    """Workout management page for trainers"""
    st.header("💪 Workout Management")
    
    # Create new workout
    with st.expander("➕ Create New Workout", expanded=False):
        with st.form("create_workout_form"):
            title = st.text_input("Workout Title")
            description = st.text_area("Description")
            
            st.subheader("Exercises")
            num_exercises = st.number_input("Number of exercises", min_value=1, max_value=20, value=3)
            
            exercises = []
            for i in range(int(num_exercises)):
                st.markdown(f"**Exercise {i+1}**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    ex_name = st.text_input(f"Exercise name", key=f"ex_name_{i}")
                with col2:
                    ex_sets = st.text_input(f"Sets/Duration", key=f"ex_sets_{i}")
                with col3:
                    ex_reps = st.text_input(f"Reps/Notes", key=f"ex_reps_{i}")
                
                if ex_name:
                    exercises.append({
                        "name": ex_name,
                        "sets": ex_sets,
                        "reps": ex_reps
                    })
            
            submit = st.form_submit_button("Create Workout")
            
            if submit:
                if title and exercises:
                    success, message = create_workout(title, description, exercises)
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.error("Please provide a title and at least one exercise")
    
    # Display existing workouts
    st.subheader("Existing Workouts")
    workouts = get_workouts()
    
    if workouts:
        for workout in workouts:
            with st.expander(f"📋 {workout['title']}"):
                st.write(f"**Description:** {workout.get('description', 'N/A')}")
                st.write("**Exercises:**")
                exercises = workout.get('exercises', [])
                for i, ex in enumerate(exercises, 1):
                    st.write(f"{i}. {ex.get('name', 'N/A')} - {ex.get('sets', 'N/A')} sets x {ex.get('reps', 'N/A')} reps")
                
                if st.button(f"Delete", key=f"delete_workout_{workout['id']}"):
                    success, message = delete_workout(workout['id'])
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
    else:
        st.info("No workouts created yet. Create your first workout above!")

def meal_plan_management_page():
    """Meal plan management page for trainers"""
    st.header("🍽️ Meal Plan Management")
    
    # Create new meal plan
    with st.expander("➕ Create New Meal Plan", expanded=False):
        with st.form("create_meal_form"):
            title = st.text_input("Meal Plan Title")
            description = st.text_area("Description")
            
            st.subheader("Meals")
            num_meals = st.number_input("Number of meals", min_value=1, max_value=10, value=3)
            
            meals = []
            for i in range(int(num_meals)):
                st.markdown(f"**Meal {i+1}**")
                col1, col2 = st.columns(2)
                with col1:
                    meal_name = st.text_input(f"Meal name", key=f"meal_name_{i}")
                with col2:
                    meal_time = st.text_input(f"Time", key=f"meal_time_{i}", placeholder="e.g., 8:00 AM")
                meal_items = st.text_area(f"Items/Instructions", key=f"meal_items_{i}")
                
                if meal_name:
                    meals.append({
                        "name": meal_name,
                        "time": meal_time,
                        "items": meal_items
                    })
            
            submit = st.form_submit_button("Create Meal Plan")
            
            if submit:
                if title and meals:
                    success, message = create_meal_plan(title, description, meals)
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.error("Please provide a title and at least one meal")
    
    # Display existing meal plans
    st.subheader("Existing Meal Plans")
    meal_plans = get_meal_plans()
    
    if meal_plans:
        for plan in meal_plans:
            with st.expander(f"🍽️ {plan['title']}"):
                st.write(f"**Description:** {plan.get('description', 'N/A')}")
                st.write("**Meals:**")
                meals = plan.get('meals', [])
                for i, meal in enumerate(meals, 1):
                    st.write(f"{i}. **{meal.get('name', 'N/A')}** ({meal.get('time', 'N/A')})")
                    st.write(f"   {meal.get('items', 'N/A')}")
                
                if st.button(f"Delete", key=f"delete_meal_{plan['id']}"):
                    success, message = delete_meal_plan(plan['id'])
                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
    else:
        st.info("No meal plans created yet. Create your first meal plan above!")

def assignment_page():
    """Assignment page for trainers to assign workouts and meal plans to clients"""
    st.header("📅 Assign to Clients")
    
    clients = get_clients()
    workouts = get_workouts()
    meal_plans = get_meal_plans()
    
    if not clients:
        st.warning("No clients registered yet.")
        return
    
    tab1, tab2 = st.tabs(["Assign Workout", "Assign Meal Plan"])
    
    with tab1:
        st.subheader("Assign Workout to Client")
        
        if not workouts:
            st.info("No workouts available. Create workouts first!")
        else:
            with st.form("assign_workout_form"):
                client = st.selectbox(
                    "Select Client",
                    options=clients,
                    format_func=lambda x: f"{x.get('full_name', 'N/A')} ({x.get('email', 'N/A')})"
                )
                workout = st.selectbox(
                    "Select Workout",
                    options=workouts,
                    format_func=lambda x: x.get('title', 'N/A')
                )
                assigned_date = st.date_input("Date", value=date.today())
                
                submit = st.form_submit_button("Assign Workout")
                
                if submit and client and workout:
                    success, message = assign_workout(workout['id'], client['id'], assigned_date)
                    if success:
                        st.success(message)
                    else:
                        st.error(message)
    
    with tab2:
        st.subheader("Assign Meal Plan to Client")
        
        if not meal_plans:
            st.info("No meal plans available. Create meal plans first!")
        else:
            with st.form("assign_meal_form"):
                client = st.selectbox(
                    "Select Client",
                    options=clients,
                    format_func=lambda x: f"{x.get('full_name', 'N/A')} ({x.get('email', 'N/A')})",
                    key="meal_client_select"
                )
                meal_plan = st.selectbox(
                    "Select Meal Plan",
                    options=meal_plans,
                    format_func=lambda x: x.get('title', 'N/A')
                )
                assigned_date = st.date_input("Date", value=date.today(), key="meal_date_input")
                
                submit = st.form_submit_button("Assign Meal Plan")
                
                if submit and client and meal_plan:
                    success, message = assign_meal_plan(meal_plan['id'], client['id'], assigned_date)
                    if success:
                        st.success(message)
                    else:
                        st.error(message)

def client_dashboard():
    """Display client dashboard"""
    st.title(f"👋 Welcome, {st.session_state.profile.get('full_name', 'Client')}")
    
    if st.sidebar.button("Logout"):
        sign_out()
        st.rerun()
    
    st.header("📅 Today's Checklist")
    st.write(f"**Date:** {date.today().strftime('%A, %B %d, %Y')}")
    
    workout_assignments, meal_assignments = get_today_assignments()
    
    # Display workouts
    st.subheader("💪 Workouts")
    if workout_assignments:
        for assignment in workout_assignments:
            workout = assignment.get('workouts', {})
            with st.expander(f"{'✅' if assignment.get('completed') else '⬜'} {workout.get('title', 'N/A')}", expanded=not assignment.get('completed')):
                st.write(f"**Description:** {workout.get('description', 'N/A')}")
                st.write("**Exercises:**")
                exercises = workout.get('exercises', [])
                for i, ex in enumerate(exercises, 1):
                    st.write(f"{i}. {ex.get('name', 'N/A')} - {ex.get('sets', 'N/A')} sets x {ex.get('reps', 'N/A')} reps")
                
                completed = st.checkbox(
                    "Mark as complete",
                    value=assignment.get('completed', False),
                    key=f"workout_{assignment['id']}"
                )
                
                if completed != assignment.get('completed', False):
                    if mark_workout_complete(assignment['id'], completed):
                        st.rerun()
    else:
        st.info("No workouts assigned for today.")
    
    # Display meals
    st.subheader("🍽️ Meal Plans")
    if meal_assignments:
        for assignment in meal_assignments:
            meal_plan = assignment.get('meal_plans', {})
            with st.expander(f"{'✅' if assignment.get('completed') else '⬜'} {meal_plan.get('title', 'N/A')}", expanded=not assignment.get('completed')):
                st.write(f"**Description:** {meal_plan.get('description', 'N/A')}")
                st.write("**Meals:**")
                meals = meal_plan.get('meals', [])
                for i, meal in enumerate(meals, 1):
                    st.write(f"{i}. **{meal.get('name', 'N/A')}** ({meal.get('time', 'N/A')})")
                    st.write(f"   {meal.get('items', 'N/A')}")
                
                completed = st.checkbox(
                    "Mark as complete",
                    value=assignment.get('completed', False),
                    key=f"meal_{assignment['id']}"
                )
                
                if completed != assignment.get('completed', False):
                    if mark_meal_complete(assignment['id'], completed):
                        st.rerun()
    else:
        st.info("No meal plans assigned for today.")

# Main app
def main():
    """Main application entry point"""
    if not st.session_state.user:
        login_page()
    else:
        # Check if we have profile data
        if not st.session_state.profile:
            st.error("Error loading profile. Please try logging in again.")
            sign_out()
            st.rerun()
            return
        
        # Route based on user role
        role = st.session_state.profile.get('role')
        if role == 'trainer':
            trainer_dashboard()
        elif role == 'client':
            client_dashboard()
        else:
            st.error("Invalid user role")
            sign_out()

if __name__ == "__main__":
    main()
