import { useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import './App.css';
import Button from 'react-bootstrap/Button';

function App() {


  const [firstName] = useState("Alex")
  const [middleName] = useState("");
  const [lastName] = useState("");
  const [gender] = useState("");
  const [dob] = useState("");
  const [country] = useState("");
  const [degreeType] = useState("");

  return (
    <Tabs
      defaultActiveKey="profile"
      id="uncontrolled-tab-example"
      className="w-100"
    >
      <Tab eventKey="home" title="Home">
        Tab content for Home
      </Tab>
      <Tab eventKey="student" title="Student">  
        {firstName}
      </Tab>
      <Tab eventKey="validation" title="Validation">
        Tab content for Validation Flow
      </Tab>
    </Tabs>
  )
}

export default App
