'use client'
import React, { useState } from 'react';

export default function ImageRecommendation() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setRecommendations([]);
    setError(null);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!selectedFile) {
      setError("Please upload an image first.");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append("file", selectedFile);

      // Backend API endpoint
      const response = await fetch('http://127.0.0.1:8000/recommend/', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to fetch recommendations");
      }

      const data = await response.json();
      // data.recommendations expected to be an array with {filename, name, score}

      setRecommendations(data.recommendations || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20 }}>
      <h2>Image-based Product Recommendation</h2>
      <form onSubmit={handleSubmit}>
        <input className='border-2 border-black cursor-pointer text-blue-950' type="file" accept="image/*" onChange={handleFileChange} />
        <button className='border-2 border-black cursor-pointer' type="submit" disabled={loading} style={{ marginLeft: 10 }}>
          {loading ? "Loading..." : "Get Recommendations"}
        </button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      <div style={{ marginTop: 20 }}>
        {recommendations.length > 0 ? (
          <div>
            <h3>Recommended Products:</h3>
            <ul style={{ listStyle: 'none', padding: 0 }}>
              {recommendations.map((item, index) => (
                <li key={index} style={{ marginBottom: 10, display: 'flex', alignItems: 'center' }}>
                  <img
                    src={`http://127.0.0.1:8000/images/${item.filename}`} // <-- Construct full URL here
                    alt={item.name}
                    style={{ width: 100, height: 100, objectFit: 'contain', marginRight: 10 }}
                  />
                  <div>
                    <div>{item.name}</div>
                    <div style={{ fontSize: 12, color: 'gray' }}>
                      Similarity score: {item.score.toFixed(3)}
                    </div>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        ) : (
          !loading && <p>No recommendations yet.</p>
        )}
      </div>
    </div>
  );
}
