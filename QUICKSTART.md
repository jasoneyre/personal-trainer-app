# Quick Start Guide

## What You've Built

This is a **Personal Trainer MVP** application with the following features:

### For Trainers:
1. **Workout Management**
   - Create workouts with multiple exercises
   - Each exercise includes name, sets, and reps
   - Delete workouts you've created

2. **Meal Plan Management**
   - Create meal plans with multiple meals
   - Each meal includes name, time, and items/instructions
   - Delete meal plans you've created

3. **Client Assignment**
   - Assign workouts to clients by date
   - Assign meal plans to clients by date
   - View all registered clients

### For Clients:
1. **Today's Checklist**
   - See all workouts assigned for today
   - See all meal plans assigned for today
   - Mark workouts as complete with checkboxes
   - Mark meals as complete with checkboxes
   - Visual indicators (✅ for complete, ⬜ for incomplete)

## Architecture

```
┌─────────────────┐
│   Streamlit     │  ← User Interface (Single Page App)
│   (app.py)      │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│   Supabase      │  ← Backend (Database + Auth)
│                 │
│  - Auth         │  ← User authentication
│  - PostgreSQL   │  ← Data storage
│  - RLS Policies │  ← Row Level Security
└─────────────────┘
```

## Database Schema

**Tables:**
- `profiles` - User information (extends Supabase auth.users)
- `workouts` - Workout templates created by trainers
- `meal_plans` - Meal plan templates created by trainers
- `workout_assignments` - Links workouts to clients by date
- `meal_assignments` - Links meal plans to clients by date

**Security:**
- Row Level Security (RLS) ensures trainers only see their own data
- Clients only see workouts/meals assigned to them
- Authentication required for all operations

## Testing the Application

### Option 1: With Real Supabase Backend

1. Follow the setup instructions in README.md
2. Create a Supabase project
3. Run the schema.sql in Supabase SQL Editor
4. Configure your .env file
5. Run `streamlit run app.py`

### Option 2: Demo Mode (Without Supabase)

The application requires Supabase to function. There is no demo/offline mode as all data is stored in Supabase.

## User Flows

### Trainer Flow:
```
1. Sign up as trainer
2. Create workouts and meal plans
3. Wait for clients to sign up
4. Go to "Assign to Clients"
5. Select client, workout/meal, and date
6. Assignment is now visible to client on that date
```

### Client Flow:
```
1. Sign up as client
2. View "Today's Checklist" (initially empty)
3. When trainer assigns items, they appear on assigned date
4. Click on each item to expand details
5. Check "Mark as complete" when done
```

## Common Use Cases

### Scenario 1: Weekly Workout Plan
Trainer creates 7 different workouts and assigns one to each client for each day of the week.

### Scenario 2: Meal Prep Plan
Trainer creates a meal plan and assigns it to multiple clients for the same dates.

### Scenario 3: Progressive Training
Trainer assigns increasing difficulty workouts to a client over time, tracking completion.

## Next Steps for Enhancement

### Potential Features to Add:
1. **Calendar View** - See assignments across multiple days
2. **Progress Tracking** - Charts and statistics for completed workouts
3. **Messaging** - Communication between trainer and client
4. **Exercise Library** - Pre-built exercises to choose from
5. **Nutrition Tracking** - Calorie and macro tracking
6. **Photo Upload** - Progress photos
7. **Workout History** - See past completed workouts
8. **Client Dashboard for Trainers** - See all clients' progress
9. **Notifications** - Email/SMS reminders for assignments
10. **Payment Integration** - Subscription management

### Code Improvements:
- Add unit tests
- Add error handling for network issues
- Add loading indicators
- Add data validation
- Optimize database queries
- Add caching for better performance
- Add export functionality (PDF reports)

## Technical Details

### Dependencies:
- **streamlit** - Web framework for the UI
- **supabase** - Backend as a Service (BaaS)
- **python-dotenv** - Environment variable management

### File Structure:
```
personal-trainer-app/
├── app.py              # Main application (all code)
├── schema.sql          # Database schema
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
├── .gitignore         # Git ignore rules
└── README.md          # Setup documentation
```

### Session State:
Streamlit uses session state to maintain:
- `user` - Current authenticated user
- `profile` - User profile with role information

### Authentication:
- Email/password via Supabase Auth
- Email verification required
- Role-based routing (trainer vs client)

## Troubleshooting

**Q: Why does the app show an error about SUPABASE_URL?**
A: You need to create a .env file with your Supabase credentials.

**Q: Why can't I see any clients as a trainer?**
A: Clients need to sign up first. Have them create accounts with role="client".

**Q: Why don't I see any assignments as a client?**
A: Your trainer needs to assign workouts/meals to you first.

**Q: Can I change my role from client to trainer?**
A: Not through the UI. You'd need to update it directly in the Supabase database.

**Q: How do I reset my password?**
A: Currently not implemented. You'd need to use Supabase's password reset features.

## Support

For issues or questions:
1. Check the README.md for setup instructions
2. Review the schema.sql for database structure
3. Check Supabase dashboard for authentication issues
4. Review browser console for JavaScript errors
5. Open an issue on GitHub

---

**Built with ❤️ using Streamlit and Supabase**
