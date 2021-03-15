import './App.css';
import Help from'./components/Help'
import AboutUs from './components/AboutUs'
import Home from './components/Home'
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Mask from './components/Mask'
// import Form from './components/Form';
import Login from './components/login';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

function App() {
 // const [token, setToken] = useState('');

  //const userLogin = (tok) => {
   // setToken(tok);
//  }

  return (
    <Router>
      <div className="App"> 
         
         {/* <Navbar/> */}
         <Navbar  />
        
         <Switch>
            <Route path="/" exact component = {Home}/>
            <Route path="/aboutus" component = {AboutUs}/>
            <Route path="/mask" component = {Mask}/>
            <Route path="/help" component = {Help}/>  
            <Route path="/login" component = {Login}/> 
         </Switch>
         <Footer/>
      </div>
    </Router>

  );
}

export default App;
