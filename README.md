# Personal Trainer App 💪

A minimal Streamlit + Supabase MVP that lets trainers create workouts and meal plans, assign them to clients by date, and lets clients view a "Today" checklist and mark items done.

## Features

### For Trainers
- 📋 Create and manage workouts with exercises
- 🍽️ Create and manage meal plans
- 📅 Assign workouts and meal plans to clients by date
- 👥 View all registered clients

### For Clients
- 📅 View today's assigned workouts and meal plans
- ✅ Mark workouts and meals as complete
- 📊 Track daily progress

## Technology Stack

- **Frontend:** Streamlit
- **Backend:** Supabase (PostgreSQL + Auth)
- **Language:** Python 3.8+

## Prerequisites

- Python 3.8 or higher
- A Supabase account (free tier available at https://supabase.com)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jasoneyre/personal-trainer-app.git
cd personal-trainer-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Supabase

1. Go to https://supabase.com and create a new project
2. Wait for the database to be provisioned
3. Go to the SQL Editor in your Supabase dashboard
4. Copy the contents of `schema.sql` and run it in the SQL Editor
5. This will create all necessary tables, indexes, and security policies

### 4. Configure Environment Variables

1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Get your Supabase credentials:
   - Go to your Supabase project settings
   - Navigate to API settings
   - Copy your project URL and anon/public key

3. Update your `.env` file with your credentials:
   ```
   SUPABASE_URL=your_actual_supabase_url
   SUPABASE_KEY=your_actual_supabase_anon_key
   ```

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Usage Guide

### First Time Setup

1. **Create a Trainer Account:**
   - Click on the "Sign Up" tab
   - Enter your email, password, and full name
   - Select "trainer" from the dropdown
   - Click "Sign Up"
   - Verify your email (check your inbox)

2. **Create Client Accounts:**
   - Clients can sign up on their own by selecting "client" during registration
   - Or you can create accounts for them

### For Trainers

1. **Create Workouts:**
   - Navigate to "Workouts" in the sidebar
   - Click "Create New Workout"
   - Enter workout title, description, and exercises
   - Each exercise should have a name, sets, and reps

2. **Create Meal Plans:**
   - Navigate to "Meal Plans" in the sidebar
   - Click "Create New Meal Plan"
   - Enter meal plan title, description, and meals
   - Each meal should have a name, time, and items/instructions

3. **Assign to Clients:**
   - Navigate to "Assign to Clients" in the sidebar
   - Select a client from the dropdown
   - Choose a workout or meal plan
   - Pick a date for the assignment
   - Click "Assign"

### For Clients

1. **View Today's Plan:**
   - After logging in, you'll see "Today's Checklist"
   - This shows all workouts and meal plans assigned for today

2. **Complete Items:**
   - Click on each workout or meal plan to expand details
   - Check the "Mark as complete" box when done
   - The item will be marked with a ✅ checkmark

## Database Schema

The app uses the following main tables:

- **profiles:** User information and roles (trainer/client)
- **workouts:** Workout templates created by trainers
- **meal_plans:** Meal plan templates created by trainers
- **workout_assignments:** Links workouts to clients by date
- **meal_assignments:** Links meal plans to clients by date

All tables include Row Level Security (RLS) policies to ensure data privacy and proper access control.

## Security Features

- 🔐 Email/password authentication via Supabase Auth
- 🛡️ Row Level Security (RLS) policies
- 👤 Role-based access control (trainer vs client)
- 🔒 Secure password storage
- ✉️ Email verification for new accounts

## Development

### Project Structure

```
personal-trainer-app/
├── app.py              # Main Streamlit application
├── schema.sql          # Database schema and RLS policies
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

### Adding New Features

The app is designed to be minimal but extensible. Common extensions might include:
- Progress tracking and analytics
- Exercise libraries and templates
- Nutrition tracking
- Calendar view for multiple days
- Messaging between trainers and clients
- Photo uploads for progress tracking

## Troubleshooting

**Issue:** "Please set SUPABASE_URL and SUPABASE_KEY in your .env file"
- **Solution:** Make sure you've created a `.env` file with your Supabase credentials

**Issue:** Database errors or permission denied
- **Solution:** Ensure you've run the `schema.sql` file in your Supabase SQL Editor

**Issue:** Can't log in after signing up
- **Solution:** Check your email for the verification link from Supabase

**Issue:** Assignments not showing up for clients
- **Solution:** Make sure the assignment date matches today's date

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.
