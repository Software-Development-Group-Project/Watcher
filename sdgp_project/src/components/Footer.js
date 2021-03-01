import React from 'react';
import '../CSS/footer.css';
import {ReactComponent as Facebook} from '../images/social/facebook.svg';
import {ReactComponent as Insta} from '../images/social/instagram.svg';
import {ReactComponent as Youtube} from '../images/social/youtube.svg';
import {ReactComponent as LinkedIn} from '../images/social/linkedin.svg';
import {ReactComponent as Twitter} from '../images/social/twitter.svg';
import { Link } from 'react-router-dom';

class Footer extends React.Component{
    render(){
        return (
            <footer className="footer">
                <div className="footer-left">
                    <p className="text">Watcher is created for accademic purpose only for Informatics Institute of Technology and University of Westminster.</p>
                    <div class="socials">
                        <a href="https://www.facebook.com/comicbookdotcom"><Facebook className="logo"/></a>
                        <a href='https://www.instagram.com/comicbook/'><Insta className="logo"/></a>
                        <a href='https://www.youtube.com/user/ComicBookCom/playlists'><Youtube className="logo"/></a>
                        <a href='https://www.youtube.com/user/ComicBookCom/playlists'><LinkedIn className="logo"/></a>
                        <a href='https://twitter.com/ComicBook'><Twitter className="logo"/></a>
                    </div>
                </div>
                <ul className="footer-right">
                    <li class="group-links">
                        <h4>Features</h4>
                        <ul className="box">
                            <li><a href="fg">Live</a></li>
                            <li><a href="fg">Submit</a></li>
                            <li><Link to="/form">Login</Link></li>
                            <li><a href="fg">Sign Up</a></li>
                        </ul>
                    </li>
                    <li className="group-links">
                        <h4>Pages</h4>
                        <ul className="box">
                          <Link to="/">
                            <li>Home</li>
                          </Link>
                            <li>Mask Detection</li>
                          <Link to="/aboutus">
                             <li>About US</li>
                          </Link>
                          <Link to="/help">
                             <li>Help</li>
                          </Link>
                        </ul>
                    </li>
                    <li className="group-links">
                        <h4>Address</h4>
                        <ul className="box">
                            <li>57, Ramakrishna Road</li>
                            <li>Colombo 06</li>
                            <li>Sri Lanka</li>
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