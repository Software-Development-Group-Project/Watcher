import React from 'react';
import '../CSS/welcome.css';
import social_distance from '../images/social_distance.svg';

class Welcome extends React.Component{
    render(){
        return (
            <div id="welcome-page">
                <div id="welcome-container">
                    
                    <div id="welcome-info-container">
                        <h1>Welcome to <span class="special-text">Watcher</span></h1>
                        <p>In this hard times closing and lockdowns are not easy at all instead if people follow the rules and stop spreading virus would be the better way to live the normal  day to day life. But some people don't follow any rules and regulations for them it's easy to have some one to manage them. <span class="special-text">Watcher</span> will do that work for you!</p>
                        <div class="group-links">
                            <a href="#" class="link">Sign In</a>
                            <a href="#" class="link">Sign Up</a>
                        </div>
                    </div>

                    <div id="welcome-img-container">
                        <img src={social_distance} alt="Wearing mask and maintaining social distance"/>
                    </div>

                </div>
            </div>
        );
    }
}

export default Welcome;