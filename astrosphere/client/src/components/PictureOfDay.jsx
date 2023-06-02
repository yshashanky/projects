import React, {useState, useEffect} from "react";

function PictureOfDay() {

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
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    if (!data) {
        return null;
    }

    return (
        <div>
            {console.log(data)}
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );

}

export default PictureOfDay;