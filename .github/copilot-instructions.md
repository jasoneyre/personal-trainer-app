# Personal Trainer Application - AI Coding Guide

## Project Overview
Streamlit web app for personal trainers and clients. **Tech Stack**: Streamlit + Supabase (auth + Postgres + storage). Progressive Web App that works on mobile Safari/Chrome without app store deployment.

## Core Architecture
**Two-Role System**:
- **Trainer**: Create workout/meal templates, assign to clients, track progress, messaging
- **Client**: View assigned plans, check off completed sets/meals, progress tracking

## Tech Stack Details
- **Frontend**: Streamlit (Python web framework)
- **Backend**: Supabase (PostgreSQL + Auth + Row-Level Security + Storage)
- **Auth**: Supabase Auth with role-based access (trainer|client)
- **Deploy**: Streamlit Cloud or similar (single command deployment)
- **Mobile**: PWA - add to home screen on iOS/Android

## Data Model (Minimal MVP)
Core tables in Supabase:
- `users(id, role, name, email)` - Auth + role management
- `clients(id, trainer_id, name, goals, allergens)` - Client profiles
- `exercises(id, name, muscle_group, equipment, cues)` - Exercise library
- `workout_templates/workout_blocks/workout_sets` - Program structure
- `meal_plans/meals/meal_items(food, qty, macros)` - Nutrition plans
- `assignments(client_id, plan_id, type, date)` - Daily assignments
- `checkins(client_id, date, weight, energy, notes)` - Progress tracking
- `messages(trainer_id, client_id, body, created_at)` - Communication

## Development Workflow

### Project Structure
```
/app.py                 # Main Streamlit entry point
/pages/                 # Streamlit pages (trainer/, client/)
  /trainer/             # Trainer dashboard, program builder, analytics
  /client/              # Client today view, progress, substitutions
/components/            # Reusable Streamlit components
/db/                    # Supabase connection, queries, schema
/utils/                 # Helper functions, auth decorators
/requirements.txt       # Python dependencies
/.env                   # Supabase keys (never commit!)
```

### Key Development Commands
- `streamlit run app.py` - Start local development
- `pip install -r requirements.txt` - Install dependencies
- Database migrations via Supabase dashboard or SQL migrations

## Code Patterns

### Supabase Integration
- Use `@st.cache_resource` for Supabase client initialization
- Row-Level Security (RLS) policies enforce trainer/client data access
- Example query pattern:
```python
@st.cache_data
def get_client_assignments(client_id: str, date: str):
    return supabase.table('assignments').select('*').eq('client_id', client_id).eq('date', date).execute()
```

### Streamlit Auth Flow
- Store user session in `st.session_state`
- Use role-based page routing: trainer sees dashboard, client sees today view
- Auth decorators to protect pages by role

## Core User Flows

### Trainer Workflow
1. **Dashboard**: Overview of clients, recent activity, quick actions
2. **Exercise Library**: Manage exercises (name, muscle_group, equipment, cues)
3. **Program Builder**: Drag-drop interface to create workout/meal templates
4. **Assignment**: Assign templates to specific clients with dates
5. **Messaging**: Chat with clients, view progress notes
6. **Analytics**: Client progress charts, completion rates

### Client Workflow
1. **Today View**: See assigned workouts + meals for today
2. **Check-off**: Mark sets/meals complete, add notes/weights
3. **Substitutions**: Request exercise/food swaps from trainer
4. **Progress**: View historical data, weight tracking, energy levels

## Privacy & Compliance (EU/GDPR)
- **Supabase Auth + RLS**: Automatic data isolation by user role
- **Data Encryption**: Encrypt sensitive notes and health data
- **User Rights**: Export/delete functionality for GDPR compliance
- **Minimal PHI**: Store only necessary health information
- **Audit Logs**: Track data access and modifications

## Performance & Mobile
- **PWA Setup**: Configure manifest.json for "Add to Home Screen"
- **Responsive Design**: Use Streamlit columns for mobile layout
- **Caching**: Aggressive use of `@st.cache_data` for database queries
- **Offline Support**: Consider IndexedDB for workout logging when offline

## Nice-to-Have Features
- **Progress Charts**: Streamlit's native charting for weight/strength trends
- **Push Notifications**: Email reminders via Supabase Edge Functions
- **File Uploads**: PDF meal plans stored in Supabase Storage
- **Calendar Sync**: Google Calendar integration for workout scheduling
- **Photo Uploads**: Progress photos with before/after comparisons

## Deployment Strategy
- **Streamlit Cloud**: One-click deploy from GitHub
- **Environment Variables**: Supabase URL/keys in Streamlit secrets
- **Domain Setup**: Custom domain for professional appearance
- **SSL**: Automatic HTTPS via Streamlit Cloud
- **Monitoring**: Built-in Streamlit analytics + Supabase dashboard

## Getting Started Checklist
1. Set up Supabase project (database + auth)
2. Configure Row-Level Security policies
3. Create initial table schema
4. Build basic auth flow in Streamlit
5. Implement trainer dashboard MVP
6. Add client "Today" view
7. Deploy to Streamlit Cloud
8. Configure PWA settings

---
*Update this file as new patterns emerge in the actual implementation.*