// // 

// import React from 'react';
// import { Link } from 'react-router-dom';
// import styled from 'styled-components';

// const HeaderWrapper = styled.header`
//   background-color: #2c3e50;
//   padding: 0 20px;
//   display: flex;
//   justify-content: space-between;
//   align-items: center;
//   height: 70px;
// `;

// const Title = styled.h1`
//   color: #e74c3c;
//   font-family: 'Helvetica', sans-serif;
//   font-size: 2.5em;
//   margin: 0;
// `;

// const Nav = styled.nav`
//   ul {
//     list-style-type: none;
//     display: flex;
//     gap: 20px;
//   }
// `;

// const StyledLink = styled(Link)`
//   color: #1abc9c;
//   text-decoration: none;
//   font-weight: bold;
//   position: relative;

//   &:after {
//     content: '';
//     position: absolute;
//     width: 0;
//     height: 2px;
//     bottom: -3px;
//     left: 0;
//     background-color: #1abc9c;
//     transition: width 0.3s;
//   }

//   &:hover:after {
//     width: 100%;
//   }
// `;

// function Header() {
//   return (
//     <HeaderWrapper>
//       <Title>Latent Homer</Title>
//       <Nav>
//         <ul>
//           <li><StyledLink to="/">Simpsons Embedding Search</StyledLink></li>
//           <li><StyledLink to="/darts">Vibe Darts</StyledLink></li>
//         </ul>
//       </Nav>
//     </HeaderWrapper>
//   );
// }

// export default Header;

import React from 'react';
import styled from 'styled-components';

const HeaderWrapper = styled.header`
  background-color: #2c3e50;
  padding: 0 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70px;
`;

const Title = styled.h1`
  color: #e74c3c;
  font-family: 'Helvetica', sans-serif;
  font-size: 2.5em;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
`;

function Header() {
  return (
    <HeaderWrapper>
      <Title>Latent Homer</Title>
    </HeaderWrapper>
  );
}

export default Header;