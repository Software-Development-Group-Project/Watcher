import React from 'react';
import './footer.css';
import {ReactComponent as Facebook} from '../../assets/social/facebook.svg';
import {ReactComponent as Insta} from '../../assets/social/instagram.svg';
import {ReactComponent as Youtube} from '../../assets/social/youtube.svg';
import {ReactComponent as LinkedIn} from '../../assets/social/linkedin.svg';
import {ReactComponent as Twitter} from '../../assets/social/twitter.svg';


class Footer extends React.Component{
    render(){
        return (
            <footer className="footer">
                <div className="footer-left">
                    <p className="text">Watcher is created for accademic purpose only for Informatics Institute of Technology and University of Westminster.</p>
                    <div class="socials">
                        <a><Facebook className="logo"/></a>
                        <a><Insta className="logo"/></a>
                        <a><Youtube className="logo"/></a>
                        <a><LinkedIn className="logo"/></a>
                        <a><Twitter className="logo"/></a>
                    </div>
                </div>
                <ul className="footer-right">
                    <li class="group-links">
                        <h2>Features</h2>
                        <ul className="box">
                            <li><a>link</a></li>
                            <li><a>link</a></li>
                            <li><a>link</a></li>
                            <li><a>link</a></li>
                            <li><a>link</a></li>
                        </ul>
                    </li>
                    <li className="group-links">
                        <h2>Sites</h2>
                        <ul className="box">
                            <li><a>link</a></li>
                            <li><a>link</a></li>
                            <li><a>link</a></li>
                            <li><a>link</a></li>
                            <li><a>link</a></li>
                        </ul>
                    </li>
                    <li className="group-links">
                        <h2>Address</h2>
                        <ul className="box">
                            <li><a>57, Ramakrishna Road</a></li>
                            <li><a>Colombo 06</a></li>
                            <li><a>Sri Lanka</a></li>
                        </ul>
                    </li>
                </ul>
                <div className="footer-bottom">
                    <p>All rights reserved by &copy; Watcher 2021</p>
                </div>
            </footer>
        );
    }
}export default Footer;