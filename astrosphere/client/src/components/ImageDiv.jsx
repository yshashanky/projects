import React from "react";
// import Switch from '@mui/material/Switch';
import Button from '@mui/material/Button';

function ImageDiv(data){

    const imageData = data['dat'];
    
    function openImageInNewTab(){
        window.open(imageData.hdimage, '_blank')
    };

    return(
        <div>
            <img src={imageData.image} alt={imageData.title}/>
            <button onClick={openImageInNewTab}>HD Image</button>
            <Button variant="contained" target="_blank" href="http://www.google.com/">Google</Button>
        </div>
    );
};

export default ImageDiv;