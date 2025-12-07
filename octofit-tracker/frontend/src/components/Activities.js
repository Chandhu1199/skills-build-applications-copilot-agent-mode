import React, { useState, useEffect } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
        console.log('Fetching activities from:', apiUrl);
        
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Activities API response:', data);
        
        // Handle both paginated (.results) and plain array responses
        const activitiesList = data.results || data;
        setActivities(Array.isArray(activitiesList) ? activitiesList : []);
        
      } catch (error) {
        console.error('Error fetching activities:', error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) return <div className="alert alert-info">Loading activities...</div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Activities</h2>
      {activities.length === 0 ? (
        <div className="alert alert-warning">No activities found</div>
      ) : (
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>User</th>
              <th>Activity Type</th>
              <th>Distance (km)</th>
              <th>Duration (min)</th>
              <th>Calories Burned</th>
              <th>Description</th>
              <th>Created</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity) => (
              <tr key={activity._id}>
                <td>{activity.user?.username || 'Unknown'}</td>
                <td>{activity.activity_type}</td>
                <td>{activity.distance}</td>
                <td>{activity.duration}</td>
                <td>{activity.calories_burned}</td>
                <td>{activity.description}</td>
                <td>{new Date(activity.created_at).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Activities;
