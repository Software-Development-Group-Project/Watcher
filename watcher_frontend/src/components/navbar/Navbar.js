import React, { Component } from 'react'
import { MenuItems } from './MenuItems'
import './navbar.css'
import {ReactComponent as Bars} from '../../assets/bars-solid.svg';
import {ReactComponent as Cross} from '../../assets/times-solid.svg';
import {ReactComponent as Logo} from '../../assets/face-mask.svg';

class Navbar extends Component {

    state = { clicked:false}

    handleClick = ()=>{
        this.setState({ clicked: !this.state.clicked})
        console.log(this.state);
    }

    render() {
        return (
            <nav className="navbar">
                <Logo className="navbar-logo"/>
                <ul className={this.state.clicked ? 'nav-menu active' : 'nav-menu'}>
                    {MenuItems.map((item, index) => {
                        return(
                            <li key={index}>
                                <a className={item.cName} href={item.url}>
                                    {item.title}
                                </a>
                            </li> 
                        )
                    })}
                </ul>
                <div className="menu-icon" onClick={this.handleClick}>
                    {this.state.clicked ? <Cross className="bars"/>:<Bars className="bars"/>}
                </div>
            </nav>
        )
    }
}

export default Navbar
