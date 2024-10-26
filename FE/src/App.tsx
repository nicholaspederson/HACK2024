import { useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs'
import Button from 'react-bootstrap/Button';
import './App.css'
import { Col, Dropdown, Row } from 'react-bootstrap';
import Form from 'react-bootstrap/Form';

function App() {


  const [firstName] = useState("Alex")
  const [middleName] = useState("");
  const [lastName] = useState("");
  const [gender] = useState("");
  const [dob] = useState("");
  const [country] = useState("");
  const [degreeType] = useState("");

  function submitStudentData(){
    let studentData = {firstName:firstName, middleName:middleName, lastName:lastName,
      gender:gender, dob:dob, country:country, degreeType:degreeType
    }
    
    
    console.log(studentData);
    return studentData;
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

        <Form>
          <Row className="mb-3">
            <Col className="mb-3">
            <Form.Group className="mb-3" controlId="firstNameCon">
                <Form.Label>First Name</Form.Label>
                <Form.Control type="firstName" placeholder="First Name" />
              </Form.Group>
              <Form.Group className="mb-3" controlId="middleNameCon">
                <Form.Label>Middle Name</Form.Label>
                <Form.Control type="middleName" placeholder="Middle Name" />
              </Form.Group>
              <Form.Group className="mb-3" controlId="lastNameCon">
                <Form.Label>Last Name</Form.Label>
                <Form.Control type="lastName" placeholder="Last Name" />
              </Form.Group>
            </Col>
              
            </Row>
              <Form.Group>
                <Form.Label>Gender</Form.Label>
                  <Form.Select aria-label="gender">
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                  </Form.Select>
              </Form.Group>

              <Form.Group>
                <Form.Label>Date of Birth</Form.Label>
                <input aria-label="Date" type="date" /> 
              </Form.Group>
        </Form>
        <Button onClick={() => submitStudentData()} variant="primary" type="submit">
        Submit
        </Button>
      </Tab>
      <Tab eventKey="validation" title="Validation">
        Tab content for Validation Flow
      </Tab>
    </Tabs>
  )
}

export default App
