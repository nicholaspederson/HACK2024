import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import './App.css'

function App() {

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
        Tab content for Student File Uploads
      </Tab>
      <Tab eventKey="validation" title="Validation">
        Tab content for Validation Flow
      </Tab>
    </Tabs>
  )
}

export default App
