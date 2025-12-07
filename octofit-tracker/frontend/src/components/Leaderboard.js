import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboards/`;
        console.log('Fetching leaderboard from:', apiUrl);
        
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Leaderboard API response:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardList = data.results || data;
        setLeaderboard(Array.isArray(leaderboardList) ? leaderboardList : []);
        
      } catch (error) {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) return <div className="alert alert-info">Loading leaderboard...</div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Leaderboard</h2>
      {leaderboard.length === 0 ? (
        <div className="alert alert-warning">No leaderboard data found</div>
      ) : (
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Team</th>
              <th>Points</th>
              <th>Activities Count</th>
              <th>Total Distance (km)</th>
              <th>Total Calories</th>
              <th>Updated</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((entry) => (
              <tr key={entry._id}>
                <td><strong>{entry.rank}</strong></td>
                <td>{entry.user?.username || 'Unknown'}</td>
                <td>{entry.team?.name || 'Unknown'}</td>
                <td>{entry.points}</td>
                <td>{entry.activities_count}</td>
                <td>{entry.total_distance}</td>
                <td>{entry.total_calories}</td>
                <td>{new Date(entry.updated_at).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Leaderboard;
