import React, { Component } from 'react';
import '../CSS/navbar.css';
import {ReactComponent as Logo} from '../images/face-mask.svg';
import { Link } from 'react-router-dom';

class Navbar extends Component {

     

     

    render() {
        return (
            <nav className="navbar">
                <Logo className="navbar-logo"/>
                <ul className="nav-menu">
                     <Link to="/">
                        <li className="nav-links"> Home </li>
                     </Link>
                     <li className="nav-links"> Mask Detection </li>
                     <Link to="/aboutus">
                        <li className="nav-links"> About US </li>
                     </Link>
                     <Link to="/help">
                        <li className="nav-links"> Help </li>
                     </Link>
                </ul>
            </nav>
        )
    }
}

export default Navbar
