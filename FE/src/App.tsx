import { useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs'
import Button from 'react-bootstrap/Button';
import './App.css'
import { Col, Dropdown, Row } from 'react-bootstrap';
import Form from 'react-bootstrap/Form';

function App() {


  const [fName, setFname] = useState("")
  const [mName, setMname] = useState("");
  const [lName, setLname] = useState("");
  const [gender, setGender] = useState("");
  const [dob, setDob] = useState("");
  const [country, setCountry] = useState("");
  const [degreeType, setDegreeType] = useState("");

  /*const [formData, setFormData] = useState({
    firstName:"",
    middleName:"",
    lastName:"",
    gender:"",
    dob:"",
    country:"",
    degreeType:"",
  })*/


  function handleSubmit(e: any) {
    e.preventDefault();
    let studentData={fName:fName, mName:mName, lName:lName, gender:gender, dob:dob, country:country, degreeType:degreeType}
    console.log(studentData);
  }

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

        <Form noValidate onSubmit={handleSubmit}>
          <Row className="mb-3">
            <Col className="mb-3">
            <Form.Group className="mb-3" controlId="firstNameCon">
                <Form.Label>First Name</Form.Label>
                <Form.Control type="text" placeholder="First Name" value={fName} onChange={(e)=>setFname(e.target.value)}/>
              </Form.Group>
              <Form.Group className="mb-3" controlId="middleNameCon">
                <Form.Label>Middle Name</Form.Label>
                <Form.Control type="middleName" placeholder="Middle Name" value={mName} onChange={(e)=>setMname(e.target.value)}/>
              </Form.Group>
              <Form.Group className="mb-3" controlId="lastNameCon">
                <Form.Label>Last Name</Form.Label>
                <Form.Control type="lastName" placeholder="Last Name" value={lName} onChange={(e)=>setLname(e.target.value)}/>
              </Form.Group>
            </Col>
              
            </Row>
              <Form.Group>
                <Form.Label>Gender</Form.Label>
                  <Form.Select aria-label="gender" value={gender} onChange={(e)=>setGender(e.target.value)}>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                  </Form.Select>
              </Form.Group>

              <Form.Group>
                <Form.Label>Date of Birth</Form.Label>
                <Form.Control type="date" placeholder="Date of Birth: " value={dob} onChange={(e)=>setDob(e.target.value)}/>
              </Form.Group>
              <Button variant="primary" type="submit">Submit</Button>
        </Form>
      </Tab>
      <Tab eventKey="validation" title="Validation">
        Tab content for Validation Flow
      </Tab>
    </Tabs>
  )
}

export default App
