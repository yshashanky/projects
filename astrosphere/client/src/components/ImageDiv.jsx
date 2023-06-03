import React from "react";

function ImageDiv(data){

    const imageData = data['dat'];

    return(
        <div className="imageBodyDiv">
            <div className="imageDiv">
            <img src={imageData.image} alt={imageData.title}/>
            </div>
        </div>
    );
};

export default ImageDiv;