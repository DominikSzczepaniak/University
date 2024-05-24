import React, { useState } from 'react';
import { Button, Modal, Box, TextField, Typography } from '@mui/material';
import { v4 as uuidv4 } from 'uuid';

import Product from './ProductInterface';

interface ProductFormProps {
    open: boolean;
    onClose: () => void;
    onSave: (product: Product) => void;
}

const style = {
    position: 'absolute' as 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

const ProductForm: React.FC<ProductFormProps> = ({ open, onClose, onSave }) => {
    const [name, setName] = useState('');
    const [type, setType] = useState('');
    const [price, setPrice] = useState('');
    const [quantity, setQuantity] = useState('');

    const handleSubmit = () => {
        const newProduct = {
            id: uuidv4(), 
            name,
            type,
            price: parseFloat(price),
            availability: true,  
            quantity: parseInt(quantity, 10),
        };
        onSave(newProduct);
        onClose(); 
    };

    return (
        <Modal
            open={open}
            onClose={onClose}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
        >
            <Box sx={style}>
                <Typography id="modal-modal-title" variant="h6" component="h2">
                    Add New Product
                </Typography>
                <TextField fullWidth label="Name" margin="normal" value={name} onChange={e => setName(e.target.value)} />
                <TextField fullWidth label="Type" margin="normal" value={type} onChange={e => setType(e.target.value)} />
                <TextField fullWidth label="Price" type="number" margin="normal" value={price} onChange={e => setPrice(e.target.value)} />
                <TextField fullWidth label="Quantity" type="number" margin="normal" value={quantity} onChange={e => setQuantity(e.target.value)} />
                <Button onClick={handleSubmit} variant="contained" sx={{ mt: 2 }}>
                    Save
                </Button>
            </Box>
        </Modal>
    );
};
