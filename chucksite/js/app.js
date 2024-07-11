import * as React from 'react';
import { Outlet } from 'react-router-dom';

import Footer from './common/footer';
import Header from './common/header';
import Section from './common/section';

export default function App() {

    return (
        <>
            <Header header_path={'/view/header'} />
            <div className='columns is-centered'>
                <Section section_path={'/view/landing_body'} />
                <div className='column'></div>
                <div className='column is-three-fifths'>
                    <Outlet />
                </div>
                <div className='column'></div>
            </div>
            <Footer footer_path={"/view/footer"} />
        </>
    )
}