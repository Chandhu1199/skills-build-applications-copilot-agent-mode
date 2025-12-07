import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
        console.log('Fetching teams from:', apiUrl);
        
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Teams API response:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsList = data.results || data;
        setTeams(Array.isArray(teamsList) ? teamsList : []);
        
      } catch (error) {
        console.error('Error fetching teams:', error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) return <div className="alert alert-info">Loading teams...</div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Teams</h2>
      {teams.length === 0 ? (
        <div className="alert alert-warning">No teams found</div>
      ) : (
        <div className="row">
          {teams.map((team) => (
            <div key={team._id} className="col-md-6 col-lg-4 mb-3">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{team.name}</h5>
                  <p className="card-text">{team.description}</p>
                  <p>
                    <strong>Leader:</strong> {team.leader?.username || 'Unknown'}
                  </p>
                  <p>
                    <strong>Members:</strong> {team.members?.length || 0}
                  </p>
                  <p className="text-muted small">
                    Created: {new Date(team.created_at).toLocaleDateString()}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Teams;
