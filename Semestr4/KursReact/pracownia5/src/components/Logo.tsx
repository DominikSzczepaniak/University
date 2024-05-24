import React from 'react';
import { Box } from '@mui/material';
import logoSrc from './logo.png'; 

interface LogoProps {
  alt?: string;
  width?: string | number;
  height?: string | number;
}

const Logo: React.FC<LogoProps> = ({ alt, width, height }) => {
  return (
    <Box component="img" src={logoSrc} alt={alt || 'Logo'} sx={{ width, height }} />
  );
};

export default Logo;
