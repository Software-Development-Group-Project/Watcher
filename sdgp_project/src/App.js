import './App.css';
import Help from'./components/Help'
import AboutUs from './components/AboutUs'
import Home from './components/Home'
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App"> 
         
         <Navbar/>
         <Switch>
            <Route path="/" exact component = {Home}/>
            <Route path="/aboutus" component = {AboutUs}/>
            <Route path="/help" component = {Help}/> 
         </Switch>
         <Footer/>       
      </div>
    </Router>

  );
}

export default App;
