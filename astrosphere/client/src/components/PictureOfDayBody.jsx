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
        image: data['url'],
        title: data['title']
    };

    const explanationData = {
        explanation: data['explanation'],
        title: data['title'],
        date: data['date'],
        hdimage: data['hdurl']
    }

    return (
        <div className="container">
            <ImageDiv dat={imageData}/>
            <ExplanationDiv data={explanationData}/>
        </div>
    );

}

export default PictureOfDayBody;