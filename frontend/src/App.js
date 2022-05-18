import { useState, useEffect } from "react";
import Axios from "axios";
import parse from "html-react-parser";

function App() {

  const [jobs, setJobs] = useState([]);

  const getdata = () => {
    Axios.get("http://127.0.0.1:5000/jobs").then(
      (response) => {
        console.log(response.data)
        setJobs(response.data)
      }
    )
  }

  return (
    <div>
      <center>
        <title>JobScore</title>
        <button onClick={getdata} ><h1>JobScore</h1> </button>
        {jobs.map((job, index) =>
          <div key={index}>
            <hr></hr>
            <div style={{}}>
              <span><h3>Job Title:</h3>    {job.title}</span><br></br>
              <span><h3>Job Url:</h3>    <a href={job.apply_url}>{job.apply_url}</a></span><br></br>
              <span><h3>Job Department:</h3>     {job.department}</span><br></br>
              <span><h3>Job Location: </h3>    {job.location}</span><br></br>
            </div>
            <span>{parse(job.description)}</span><br></br>

          </div>
        )}
      </center>
    </div>
  )
}


export default App;