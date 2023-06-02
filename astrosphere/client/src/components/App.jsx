import React, { useEffect, useRef, useState } from 'react'

function App() {

  const [backendData, setBackendData] = useState([]);

  const shouldFetchAPI = useRef(true);
  useEffect(() => {
    if(shouldFetchAPI.current){
      shouldFetchAPI.current = false;
      fetch("/api").then(
        response => response.json()
      ).then(
        data => setBackendData(data)
      )
    }
  }, []);

  return (

    <div>
      {(typeof backendData.users === 'undefined') ? 
      (<p>Loading....</p>) : (
        backendData.users.map((user, i) => {
          return <p key={i}>{user}</p>
        })
      )}
    </div>

  )
}

export default App;
