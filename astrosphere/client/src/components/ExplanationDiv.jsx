import React from "react";
import Button from '@mui/material/Button';

function ExplanationDiv(data){

    const explanationData = data['data']

    return(
        <div className="bodyDiv">
            <h1>{explanationData.title}</h1>
            <h2>{explanationData.date}</h2>
            <p>{explanationData.explanation}</p>
            <Button className="hdbutton" variant="contained" target="_blank" href={explanationData.hdimage}>High Resulation</Button>
        </div>
    );
}


export default ExplanationDiv;