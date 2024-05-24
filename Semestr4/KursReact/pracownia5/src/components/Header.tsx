import * as React from 'react';
import { AppBar, Toolbar, Typography, styled, Box } from '@mui/material';
import { AccountCircle } from '@mui/icons-material';
import Logo from './Logo';

const StyledToolbar = styled(Toolbar)({
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
});

const Header: React.FC = () => {
  const [isHovered, setIsHovered] = React.useState(false);

  return (
    <AppBar position="sticky">
      <StyledToolbar>
        <Logo alt="My Company Logo" width={200} height={100} />
        <Box
          onMouseOver={() => setIsHovered(true)}
          onMouseOut={() => setIsHovered(false)}
          sx={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }}
        >
          <AccountCircle fontSize="large" />
          {isHovered && (
            <Typography variant="subtitle1" sx={{ marginLeft: 2 }}>
              Username
            </Typography>
          )}
        </Box>
      </StyledToolbar>
    </AppBar>
  );
};

export default Header;
