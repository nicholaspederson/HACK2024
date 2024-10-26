import { useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import './App.css'
import { Col, Dropdown, Row } from 'react-bootstrap';
import Form from 'react-bootstrap/Form';




function App() {


  const [firstName] = useState("Alex")

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
          <Row className="pt-3">
            <Col className="mr-3">
              <Form.Group className="mb-3" controlId="firstNameCon">
                  <Form.Label>First Name</Form.Label>
                  <Form.Control type="firstName" placeholder="First Name" />
                </Form.Group>
            </Col>
            <Col className="mr-3">
              <Form.Group className="mb-3" controlId="middleNameCon">
                  <Form.Label>Middle Name</Form.Label>
                  <Form.Control type="middleName" placeholder="Middle Name" />
                </Form.Group>
            </Col>
            <Col className="mr-3">
                <Form.Group className="mb-3" controlId="lastNameCon">
                  <Form.Label>Last Name</Form.Label>
                  <Form.Control type="lastName" placeholder="Last Name" />
                </Form.Group>
            </Col>
          </Row>
          <Row className="pt-3">
            <Col className="mr-3">
              <Form.Group>
                  <Form.Label>Gender</Form.Label>
                    <Form.Select aria-label="gender">
                      <option value="male">Male</option>
                      <option value="female">Female</option>
                    </Form.Select>
                </Form.Group>
            </Col>
            <Col className="mr-3">
                <Form.Group>
                  <Form.Label>Date of Birth: </Form.Label>
                  <Form.Control aria-label="date" type="Date" /> 
                </Form.Group>
            </Col>
          </Row>
          <Row className="pt-5">
            <Col className="mb-3">
                  <Form.Group>
                    <Form.Label>Country of Education</Form.Label>
                    <Form.Control type="country" placeholder = "Country" />
                  </Form.Group>
            </Col>
            <Col className="mr-3">
                <Form.Group>
                <Form.Label>Degree Type</Form.Label>
                  <Form.Select aria-label="degreeLevel">
                    <option value="undergraduate">Undergraduate</option>
                    <option value="graduateCertificate">Graduate Certificate</option>
                    <option value="masters">Masters</option>
                    <option value="doctoral">Doctoral</option>
                  </Form.Select>
                </Form.Group>
            </Col>

          
  

              




          </Row>
        </Form>
      </Tab>
      <Tab eventKey="validation" title="Validation">
        Tab content for Validation Flow
      </Tab>
    </Tabs>
  )
}

export default App
