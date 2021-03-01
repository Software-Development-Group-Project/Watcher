import React, { Component } from 'react';
import '../CSS/navbar.css';
import {ReactComponent as Logo} from '../images/face-mask.svg';
import { Link } from 'react-router-dom';

class Navbar extends Component {

     
    state = { clicked:false}

    handleClick = () => {
        this.setState({ clicked: !this.state.clicked})
    }

    render() {
        return (
            <nav className="navbar">
                <Logo className="navbar-logo"/>
                <div className="menu-icon" onClick={this.handleClick}>
                    <i className={this.state.clicked ? 'fas fa-times' : 'fas fa-bars'}></i>
                </div>
                <ul onClick={this.handleClick} className={this.state.clicked ? 'nav-menu active' : 'nav-menu'}>
                     <Link className="nav-links" to="/"> 
                        <li> Home </li>
                     </Link>
                     <li className="nav-links"> Mask Detection </li>
                     <Link className="nav-links" to="/aboutus">
                        <li> About Us </li>
                     </Link>
                     <Link className="nav-links" to="/help">
                        <li> Help </li>
                     </Link>
                </ul>
            </nav>
        )
    }
}

export default Navbar
