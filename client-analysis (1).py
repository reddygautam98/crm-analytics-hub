import pandas as pd
import numpy as np
from datetime import datetime
import json

# Read the client data
data = pd.DataFrame({
    'Client ID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008', 'C009', 'C010',
                 'C011', 'C012', 'C013', 'C014', 'C015', 'C016', 'C017', 'C018', 'C019', 'C020',
                 'C021', 'C022', 'C023', 'C024', 'C025', 'C026', 'C027', 'C028', 'C029', 'C030',
                 'C031', 'C032', 'C033', 'C034', 'C035', 'C036', 'C037', 'C038', 'C039', 'C040',
                 'C041', 'C042', 'C043', 'C044', 'C045', 'C046', 'C047', 'C048', 'C049', 'C050'],
    'Client Name': ['Vance and Sons', 'Davidson, Phillips and Rush', 'Cooper-Smith', 'Woods-Vargas',
                   'Perry PLC', 'Mccarthy-Chen', 'Harris Group', 'Robinson Inc', 'Ruiz-Allen',
                   'Chambers Inc', 'Smith, Brown and Lewis', 'Young, Rose and Kim', 'Ponce LLC',
                   'Donovan and Sons', 'Blair, Walker and Mccoy', 'Everett-Heath', 'Peterson-Webb',
                   'Valdez Ltd', 'Johnson Inc', 'Martinez-Hale', 'Cunningham, Duncan and Garcia',
                   'Mitchell Ltd', 'Mann-Atkinson', 'Griffin, Johnson and Mcdonald', 'Mitchell-Savage',
                   'Morris and Sons', 'Garcia Ltd', 'Murphy-Frank', 'Randolph, Olson and Santiago',
                   'Patterson-Hicks', 'Taylor Ltd', 'Coleman Ltd', 'Ramos and Sons', 'Jones, Santos and White',
                   'Phillips, Juarez and Jones', 'Gallegos-Warren', 'Rose Inc', 'Moody-Stephens',
                   'Fuller, Hansen and Nelson', 'Blair-Hutchinson', 'Moore, Morales and Stevens',
                   'Castillo, Ware and Harmon', 'Norman, Jones and Williams', 'Watson-Henry',
                   'Miller, Rodriguez and Montoya', 'Nelson-Allen', 'Brown Ltd', 'Moss Group',
                   'Walker-Pugh', 'Randall, Castro and Dennis']
})

# Create sample tasks data
tasks = pd.DataFrame({
    'Task ID': range(1, 101),
    'Client ID': np.random.choice(data['Client ID'], 100),
    'Task Name': np.random.choice([
        'Contract Review', 'Follow-up Meeting', 'Project Proposal', 
        'Invoice Processing', 'Client Presentation', 'Documentation',
        'Quality Check', 'Status Update', 'Resource Planning', 'Budget Review'
    ], 100),
    'Status': np.random.choice(['Pending', 'In Progress', 'Completed', 'Delayed'], 100),
    'Due Date': pd.date_range(start='2025-01-01', periods=100, freq='D'),
    'Priority': np.random.choice(['High', 'Medium', 'Low'], 100)
})

# Create sample meetings data
meetings = pd.DataFrame({
    'Meeting ID': range(1, 51),
    'Client ID': np.random.choice(data['Client ID'], 50),
    'Meeting Type': np.random.choice(['Virtual', 'In-Person', 'Phone Call'], 50),
    'Date': pd.date_range(start='2025-01-01', periods=50, freq='D'),
    'Duration': np.random.choice([30, 60, 90, 120], 50),  # minutes
    'Status': np.random.choice(['Scheduled', 'Completed', 'Cancelled'], 50)
})

# Create sample communication logs
communications = pd.DataFrame({
    'Communication ID': range(1, 201),
    'Client ID': np.random.choice(data['Client ID'], 200),
    'Type': np.random.choice(['Email', 'Phone', 'Meeting', 'Video Call'], 200),
    'Date': pd.date_range(start='2025-01-01', periods=200, freq='H'),
    'Direction': np.random.choice(['Incoming', 'Outgoing'], 200)
})

# Analysis Functions
def generate_client_insights():
    insights = {
        'total_clients': len(data),
        'client_distribution': {
            'tasks_per_client': tasks['Client ID'].value_counts().describe().to_dict(),
            'meetings_per_client': meetings['Client ID'].value_counts().describe().to_dict(),
            'communications_per_client': communications['Client ID'].value_counts().describe().to_dict()
        }
    }
    return insights

def analyze_tasks():
    task_analysis = {
        'total_tasks': len(tasks),
        'status_distribution': tasks['Status'].value_counts().to_dict(),
        'priority_distribution': tasks['Priority'].value_counts().to_dict(),
        'upcoming_deadlines': tasks[tasks['Due Date'] >= datetime.now()].head(5).to_dict('records'),
        'overdue_tasks': len(tasks[tasks['Due Date'] < datetime.now()])
    }
    return task_analysis

def analyze_meetings():
    meeting_analysis = {
        'total_meetings': len(meetings),
        'type_distribution': meetings['Meeting Type'].value_counts().to_dict(),
        'status_distribution': meetings['Status'].value_counts().to_dict(),
        'upcoming_meetings': meetings[meetings['Date'] >= datetime.now()].head(5).to_dict('records'),
        'average_duration': meetings['Duration'].mean()
    }
    return meeting_analysis

def analyze_communications():
    comm_analysis = {
        'total_communications': len(communications),
        'type_distribution': communications['Type'].value_counts().to_dict(),
        'direction_distribution': communications['Direction'].value_counts().to_dict(),
        'daily_average': len(communications) / len(communications['Date'].dt.date.unique()),
        'busiest_day': communications.groupby(communications['Date'].dt.date).size().idxmax()
    }
    return comm_analysis

# Generate complete analysis
def generate_dashboard_data():
    dashboard_data = {
        'client_insights': generate_client_insights(),
        'task_analysis': analyze_tasks(),
        'meeting_analysis': analyze_meetings(),
        'communication_analysis': analyze_communications(),
        'recent_activities': {
            'recent_tasks': tasks.sort_values('Due Date', ascending=False).head(5).to_dict('records'),
            'recent_meetings': meetings.sort_values('Date', ascending=False).head(5).to_dict('records'),
            'recent_communications': communications.sort_values('Date', ascending=False).head(5).to_dict('records')
        }
    }
    return dashboard_data

# Export analysis to JSON for dashboard consumption
def export_dashboard_data():
    dashboard_data = generate_dashboard_data()
    with open('dashboard_data.json', 'w') as f:
        json.dump(dashboard_data, f, default=str, indent=4)

# Generate CSV exports for different aspects
def export_csv_reports():
    # Export task status report
    task_status = tasks.groupby('Status').agg({
        'Task ID': 'count',
        'Priority': lambda x: x.value_counts().to_dict()
    }).reset_index()
    task_status.to_csv('task_status_report.csv', index=False)
    
    # Export client activity summary
    client_activity = pd.DataFrame({
        'Client ID': data['Client ID'],
        'Total Tasks': tasks['Client ID'].value_counts(),
        'Total Meetings': meetings['Client ID'].value_counts(),
        'Total Communications': communications['Client ID'].value_counts()
    }).fillna(0)
    client_activity.to_csv('client_activity_summary.csv', index=False)
    
    # Export meeting schedule
    upcoming_meetings = meetings[meetings['Date'] >= datetime.now()].sort_values('Date')
    upcoming_meetings.to_csv('upcoming_meetings.csv', index=False)

if __name__ == "__main__":
    # Generate all reports and analysis
    export_dashboard_data()
    export_csv_reports()
    
    # Print some key metrics
    dashboard_data = generate_dashboard_data()
    print("\nKey Metrics:")
    print(f"Total Clients: {dashboard_data['client_insights']['total_clients']}")
    print(f"Total Tasks: {dashboard_data['task_analysis']['total_tasks']}")
    print(f"Total Meetings: {dashboard_data['meeting_analysis']['total_meetings']}")
    print(f"Total Communications: {dashboard_data['communication_analysis']['total_communications']}")
