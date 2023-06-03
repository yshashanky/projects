import React, {useState, useEffect} from "react";
import ExplanationDiv from './ExplanationDiv';
import ImageDiv from "./ImageDiv";

function PictureOfDayBody() {

    const [data, setData] = useState();
    const [isloading, setIsLoading] = useState();
    const [error, setError] = useState();

    useEffect(() => {
        const fetchData = async () => {
            try {
                await fetch('https://api.nasa.gov/planetary/apod?api_key=SqDvmlkP2nm7fYyiJ1wSxIhWCicRU3dEod6qM7H3')
                        .then( response => response.json())
                        .then(jsonData => setData(jsonData));
            } catch (error) {
                setError('Error fetching data please try again later');
            } finally {
                setIsLoading(false);
            }
        };

        fetchData();
    }, []);

    if (isloading) {
        return <div>Loadin...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    if (!data) {
        return null;
    }

    const imageData = {
        hdimage: data['hdurl'],
        image: data['url'],
        title: data['title']
    };

    return (
        
        <div>
            <h1>{data['title']}</h1>
            <h2>{data['date']}</h2>
            <ExplanationDiv data={data['explanation']}/>
            <ImageDiv dat={imageData}/>
        </div>
    );

}

export default PictureOfDayBody;