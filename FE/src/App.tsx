import { SetStateAction, useEffect, useRef, useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs'
import Button from 'react-bootstrap/Button';
import './App.css'
import { Col, Dropdown, Row } from 'react-bootstrap';
import Form from 'react-bootstrap/Form';

function App() {
  const [degreeProgram, setDegreeProgram] = useState("")
  const [degreeLevel, setDegreeLevel] = useState("")

  const [fName, setFname] = useState("")
  const [mName, setMname] = useState("");
  const [lName, setLname] = useState("");
  const [gender, setGender] = useState("");
  const [dob, setDob] = useState("");
  const [country, setCountry] = useState("");
  const [degreeType, setDegreeType] = useState("");

  const [nationalID, setNationalID] = useState("");
  const [transcript1, setTranscript1] = useState("")
  const [transcript2, setTranscript2] = useState("")
  const [transcript3, setTranscript3] = useState("")

  const [country1, setCountry1] = useState("")
  const [country2, setCountry2] = useState("")
  const [country3, setCountry3] = useState("")





  function nationalIDChange(e:any){
    setNationalID(e.target.files[0])
    console.log(nationalID)
  }

  function transcriptOneChange(e:any){
    setTranscript3(e.target.files[0])
    console.log(transcript1)
  }

  function transcriptTwoChange(e:any){
    setTranscript2(e.target.files[0])
    console.log(transcript2)
  }

  function transcriptThreeChange(e:any){
    setTranscript3(e.target.files[0])
    console.log(transcript3)
  }


  useEffect(() => {
    if (degreeProgram === "Associate of Arts, General Education" || degreeProgram === "Associate of Ministerial Leadership" || degreeProgram === "Bachelor of Business Administration" || degreeProgram === "Bachelor of Science, Business & Professional Leadership" || degreeProgram === "Bachelor of Science, Communication & Mass Media" || degreeProgram === "Bachelor of Science, Digital Media & Design" || degreeProgram === "Bachelor of Science, Global Education Studies" || degreeProgram === "Bachelor of Science, Human Services" || degreeProgram === "Bachelor of Science, Ministerial Leadership: Biblical Studies" || degreeProgram === "Bachelor of Science, Ministerial Leadership: Christian Ministry" || degreeProgram === "Bachelor of Science, Ministerial Leadership: Pastoral Care and Counseling" || degreeProgram === "Bachelor of Science, Organizational Leadership" || degreeProgram === "Bachelor of Science, Psychology") {
      setDegreeLevel("Undergrad");
    } else if (degreeProgram === "Post Graduate Diploma: Global Ministry Design" || degreeProgram === "Post Graduate Diploma: Human Services: Administration" || degreeProgram === "Post Graduate Diploma: Human Services: Children and Family" || degreeProgram === "Post Graduate Diploma: Leadership: Entrepreneurship" || degreeProgram === "Post Graduate Diploma: Leadership: Non-Profit" || degreeProgram === "Post Graduate Diploma: Organizational Leadership") {
      setDegreeLevel("Graduate")
    } else if (degreeProgram === "Doctorate in Strategic Leadership" || degreeProgram === "Ph.D. in Organizational Leadership" || degreeProgram === "Ph.D. in Organizational Leadership: Ministerial Leadership") {
      setDegreeLevel("Doctoral")
    } else if (degreeProgram === "") {
      setDegreeLevel("")
    } else {
      setDegreeLevel("Masters")
    }
  }, [degreeProgram])

  function handleSubmit(e: any) {
    e.preventDefault();
    let studentData = { fName: fName, mName: mName, lName: lName, gender: gender, dob: dob, degreeType: degreeType, nationalID: nationalID, transcript1: transcript1, transcript2: transcript2, transcript3: transcript3, country1: country1, country2:country2, country3: country3 }
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
          <Row className="mt-5">
            <Form.Group as={Col} className="mr-3" controlId="firstNameCon">
              <Form.Label><br/>First Name</Form.Label>
              <Form.Control type="text" placeholder="First Name" value={fName} onChange={(e) => setFname(e.target.value)} />
            </Form.Group>
            <Form.Group as={Col} className="mr-3" controlId="middleNameCon">
              <Form.Label><br/>Middle Name</Form.Label>
              <Form.Control type="middleName" placeholder="Middle Name" value={mName} onChange={(e) => setMname(e.target.value)} />
            </Form.Group>
            <Form.Group as={Col} className="mr-3" controlId="lastNameCon">
              <Form.Label><br/>Last Name</Form.Label>
              <Form.Control type="lastName" placeholder="Last Name" value={lName} onChange={(e) => setLname(e.target.value)} />
            </Form.Group>
            <Form.Group as={Col} className="mr-3" controlId="additionalNameCon">
              <Form.Label>Additional Name (maiden name, second last name, etc.)</Form.Label>
              <Form.Control required type="text" placeholder="Additional Name" />
            </Form.Group>
          </Row>
          <Row className="pt-5">
            <Form.Group as={Col} className="mr-3" controlId="gender">
              <Form.Label>Gender</Form.Label>
              <Form.Select aria-label="gender" value={gender} onChange={(e) => setGender(e.target.value)}>
                  <option value="male">Male</option>
                  <option value="female">Female</option>
              </Form.Select>
            </Form.Group>
            <Form.Group as={Col} className="mr-3" controlId="birthdate">
              <Form.Label>Date of Birth: </Form.Label>
              <Form.Control type="date" placeholder="Date of Birth: " value={dob} onChange={(e) => setDob(e.target.value)} />
            </Form.Group>
            <Form.Group as={Col} className="mr-3" controlId="email">
              <Form.Label>Email</Form.Label>
              <Form.Control type="text" placeholder="example@mail.com" />
            </Form.Group>
          </Row>
          <Row className="pt-5">
            <Form.Group as={Col} className="mr-3" controlId="degreeLevel">
              <Form.Label>Degree Program</Form.Label>
              <Form.Select aria-label="degreeLevel" value={degreeProgram} onChange={(e) => setDegreeProgram(e.target.value)}>
                <option value=""></option>
                <option value="Associate of Arts, General Education">Associate of Arts, General Education</option>
                <option value="Associate of Ministerial Leadership">Associate of Ministerial Leadership</option>
                <option value="Bachelor of Business Administration">Bachelor of Business Administration</option>
                <option value="Bachelor of Science, Business & Professional Leadership">Bachelor of Science, Business & Professional Leadership</option>
                <option value="Bachelor of Science, Communication & Mass Media">Bachelor of Science, Communication & Mass Media</option>
                <option value="Bachelor of Science, Digital Media & Design">Bachelor of Science, Digital Media & Design</option>
                <option value="Bachelor of Science, Global Education Studies">Bachelor of Science, Global Education Studies</option>
                <option value="Bachelor of Science, Human Services">Bachelor of Science, Human Services</option>
                <option value="Bachelor of Science, Ministerial Leadership: Biblical Studies">Bachelor of Science, Ministerial Leadership: Biblical Studies</option>
                <option value="Bachelor of Science, Ministerial Leadership: Christian Ministry">Bachelor of Science, Ministerial Leadership: Christian Ministry</option>
                <option value="Bachelor of Science, Ministerial Leadership: Pastoral Care and Counseling">Bachelor of Science, Ministerial Leadership: Pastoral Care and Counseling</option>
                <option value="Bachelor of Science, Organizational Leadership">Bachelor of Science, Organizational Leadership</option>
                <option value="Bachelor of Science, Psychology">Bachelor of Science, Psychology</option>
                <option value="Post Graduate Diploma: Global Ministry Design">Post Graduate Diploma: Global Ministry Design</option>
                <option value="Post Graduate Diploma: Human Services: Administration">Post Graduate Diploma: Human Services: Administration</option>
                <option value="Post Graduate Diploma: Human Services: Children and Family">Post Graduate Diploma: Human Services: Children and Family</option>
                <option value="Post Graduate Diploma: Leadership: Entrepreneurship">Post Graduate Diploma: Leadership: Entrepreneurship</option>
                <option value="Post Graduate Diploma: Leadership: Non-Profit">Post Graduate Diploma: Leadership: Non-Profit</option>
                <option value="Post Graduate Diploma: Organizational Leadership">Post Graduate Diploma: Organizational Leadership</option>
                <option value="Master of Business Administration: Executive Leadership">Master of Business Administration: Executive Leadership</option>
                <option value="Master of Business Administration: Missional Leadership">Master of Business Administration: Missional Leadership</option>
                <option value="Master of Arts, Global Ministry Design">Master of Arts, Global Ministry Design</option>
                <option value="Master of Arts, Human Services: Administration">Master of Arts, Human Services: Administration</option>
                <option value="Master of Arts, Human Services: Children & Family">Master of Arts, Human Services: Children & Family</option>
                <option value="Master of Arts, Human Services: Crisis Resiliency">Master of Arts, Human Services: Crisis Resiliency</option>
                <option value="Master of Arts, International Community Development">Master of Arts, International Community Development</option>
                <option value="Master of Arts, Leadership: Entrepreneurship">Master of Arts, Leadership: Entrepreneurship</option>
                <option value="Master of Arts, Leadership: Non-Profit Leadership">Master of Arts, Leadership: Non-Profit Leadership</option>
                <option value="Master of Arts, Leadership: Organizational Leadership">Master of Arts, Leadership: Organizational Leadership</option>
                <option value="Master of Arts, Leadership: Research">Master of Arts, Leadership: Research</option>
                <option value="Master of Arts, Biblical Studies">Master of Arts, Biblical Studies</option>
                <option value="Master of Arts, Theological Studies">Master of Arts, Theological Studies</option>
                <option value="Master of Divinity">Master of Divinity</option>
                <option value="Master of Divinity, Ministerial Leadership: Pastoral Care & Counseling">Master of Divinity, Ministerial Leadership: Pastoral Care & Counseling</option>
                <option value="Master of Science, Pastoral Care and Counseling">Master of Science, Pastoral Care and Counseling</option>
                <option value="Master of Arts, Ministerial Leadership: Spiritual Formation">Master of Arts, Ministerial Leadership: Spiritual Formation</option>
                <option value="Master of Education, Educational Leadership">Master of Education, Educational Leadership</option>
                <option value="Master of Education, Elementary Education">Master of Education, Elementary Education</option>
                <option value="Master of Education, Exceptional Student Education">Master of Education, Exceptional Student Education</option>
                <option value="Master of Education, Literacy Education">Master of Education, Literacy Education</option>
                <option value="Master of Education, Teaching English to Speakers of Other Languages">Master of Education, Teaching English to Speakers of Other Languages</option>
                <option value="Master of Education, Teaching and Learning">Master of Education, Teaching and Learning</option>
                <option value="Doctorate in Strategic Leadership">Doctorate in Strategic Leadership</option>
                <option value="Ph.D. in Organizational Leadership">Ph.D. in Organizational Leadership</option>
                <option value="Ph.D. in Organizational Leadership: Ministerial Leadership">Ph.D. in Organizational Leadership: Ministerial Leadership</option>
              </Form.Select>
            </Form.Group>
          </Row>
            <Form.Label className="pt-3 form-control-md"><br/><br/>All documents must be submitted in .pdf format. <br/>If you are unable to convert your documents to a .pdf, <br/>please email them directly to admissions@miscio.io</Form.Label>
            <Form.Group className="mt-3">
              <Form.Label htmlFor="formFileLg" className="form-label-lg">National ID</Form.Label>
              <Form.Control type="file" accept="application/pdf" onChange= {nationalIDChange}/>
            </Form.Group>
          <Row className="mt-3">
            <Form.Group as={Col} className="mr-3">
              <Form.Label htmlFor="formFileLg" className="form-label">Transcript</Form.Label>
              <Form.Control type="file" accept="application/pdf" required onChange={transcriptOneChange}/>
            </Form.Group>

            <Form.Group as={Col} className="mr-3">
              <Form.Label htmlFor="formFileLg" className="form-label">Transcript 2</Form.Label>
              <Form.Control type="file" accept="application/pdf" onChange={transcriptTwoChange}/>
            </Form.Group>
    
            <Form.Group as={Col} className="mr-3">
              <Form.Label htmlFor="formFileLg" className="form-label">Transcript 3</Form.Label>
              <Form.Control type="file" accept="application/pdf" onChange={transcriptThreeChange}/>
            </Form.Group>
          </Row>
          <Row className="mt-3">
            <Form.Group as={Col} className="mr-3" controlId="countryTranscript1">
              <Form.Label>Issuing Country</Form.Label>
              <Form.Control type="text" placeholder="Country" value={country1} onChange={(e) => setCountry1(e.target.value)}/>
            </Form.Group>
            <Form.Group as={Col} className="mr-3" controlId="countryTranscript2">
              <Form.Label>Issuing Country</Form.Label>
              <Form.Control type="text" placeholder="Country" value={country2} onChange={(e) => setCountry2(e.target.value)}/>
            </Form.Group>
            <Form.Group as={Col} className="mr-3" controlId="countryTranscript3">
              <Form.Label>Issuing Country</Form.Label>
              <Form.Control type="text" placeholder="Country" value={country3} onChange={(e) => setCountry3(e.target.value)}/>
            </Form.Group>
          </Row>
          <Row className="mt-5">
            <Button variant="primary" type="submit">Submit</Button>
          </Row>
        </Form>
      </Tab>
    </Tabs>
  )
}

export default App

