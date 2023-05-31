import React, { useEffect, useRef, useState } from 'react'

function App() {

  const [backendData, setBackendData] = useState([]);

  // useEffect(() => {
  //   fetch("/api").then(
  //     response => response.json()
  //   ).then(
  //     data => setBackendData(data)
  //   )
  // }, []);

  const shouldLog = useRef(true);
  useEffect(() => {
    if(shouldLog.current){
      shouldLog.current = false;
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
