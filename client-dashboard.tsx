import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { PieChart, Pie, Cell } from 'recharts';
import { Calendar, Clock, Users, CheckSquare, PhoneCall } from 'lucide-react';

const Dashboard = () => {
  // Sample data based on the Python script's output
  const data = {
    tasks: {
      status: [
        { name: 'Completed', value: 25 },
        { name: 'In Progress', value: 30 },
        { name: 'Pending', value: 35 },
        { name: 'Delayed', value: 10 }
      ],
      priority: [
        { name: 'High', value: 20 },
        { name: 'Medium', value: 45 },
        { name: 'Low', value: 35 }
      ]
    },
    meetings: {
      type: [
        { name: 'Virtual', value: 25 },
        { name: 'In-Person', value: 15 },
        { name: 'Phone Call', value: 10 }
      ]
    },
    communications: {
      type: [
        { name: 'Email', value: 80 },
        { name: 'Phone', value: 45 },
        { name: 'Meeting', value: 40 },
        { name: 'Video Call', value: 35 }
      ]
    }
  };

  const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

  const KeyMetrics = () => (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
      {[
        { icon: Users, label: 'Total Clients', value: '50' },
        { icon: CheckSquare, label: 'Active Tasks', value: '100' },
        { icon: Calendar, label: 'Scheduled Meetings', value: '50' },
        { icon: PhoneCall, label: 'Communications', value: '200' }
      ].map((metric, idx) => (
        <Card key={idx} className="p-4">
          <div className="flex items-center space-x-4">
            <metric.icon className="h-8 w-8 text-blue-500" />
            <div>
              <p className="text-sm text-gray-500">{metric.label}</p>
              <p className="text-2xl font-bold">{metric.value}</p>
            </div>
          </div>
        </Card>
      ))}
    </div>
  );

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Client Management Dashboard</h1>
      
      <KeyMetrics />

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Task Status Distribution</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={data.tasks.status}
                    cx="50%"
                    cy="50%"
                    outerRadius={80}
                    dataKey="value"
                    label={({name, value}) => `${name}: ${value}`}
                  >
                    {data.tasks.status.map((entry, index) => (
                      <Cell key={index} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Communication Types</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={data.communications.type}>
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="value" fill="#0088FE" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Meeting Distribution</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={data.meetings.type}
                    cx="50%"
                    cy="50%"
                    outerRadius={80}
                    dataKey="value"
                    label={({name, value}) => `${name}: ${value}`}
                  >
                    {data.meetings.type.map((entry, index) => (
                      <Cell key={index} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Task Priority Distribution</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={data.tasks.priority}>
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="value" fill="#00C49F" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Dashboard;
