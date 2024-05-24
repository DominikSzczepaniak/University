import React, { useState } from 'react';
import { Modal, Box, Button, TextField, Typography } from '@mui/material';
import { v4 as uuidv4 } from 'uuid';

import Product from './ProductInterface';

interface AddProductModalProps {
    onSave: (product: Product) => void;
}

const AddProductModal: React.FC<AddProductModalProps> = ({ onSave }) => {
    const [modalOpen, setModalOpen] = useState(false);
    const [newProduct, setNewProduct] = useState<Product>({
        id: '', // id will be set on save
        name: '',
        type: '',
        price: 0,
        availability: false,
        quantity: 0
    });

    const handleOpenModal = () => setModalOpen(true);
    const handleCloseModal = () => setModalOpen(false);

    const handleChange = (field: keyof Product) => (event: React.ChangeEvent<HTMLInputElement>) => {
        const value = event.target.value;
        setNewProduct({
            ...newProduct,
            [field]: (field === 'price' || field === 'quantity') ? parseFloat(value) : value
        });
    };

    const handleSave = () => {
        if (!newProduct.name || !newProduct.type || isNaN(newProduct.price) || isNaN(newProduct.quantity)) {
            alert('Please fill all fields correctly.');
            return;
        }
        const productToSave = {
            ...newProduct,
            id: uuidv4(),  
            availability: true  
        };
        onSave(productToSave);
        handleCloseModal();
        setNewProduct({ id: '', name: '', type: '', price: 0, availability: false, quantity: 0 }); 
    };


    const modalStyle = {
        position: 'absolute' as const,
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 400,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 4,
    };

    return (
        <>
            <Button variant="contained" color="primary" onClick={handleOpenModal}>
                Add New Product
            </Button>
            <Modal
                open={modalOpen}
                onClose={handleCloseModal}
                aria-labelledby="add-product-modal"
                aria-describedby="add-product-form"
            >
                <Box sx={modalStyle}>
                    <Typography id="add-product-modal" variant="h6" component="h2">
                        Add New Product
                    </Typography>
                    <TextField fullWidth label="Name" value={newProduct.name} onChange={handleChange('name')} margin="normal" />
                    <TextField fullWidth label="Type" value={newProduct.type} onChange={handleChange('type')} margin="normal" />
                    <TextField fullWidth label="Price" type="number" value={newProduct.price} onChange={handleChange('price')} margin="normal" />
                    <TextField fullWidth label="Quantity" type="number" value={newProduct.quantity} onChange={handleChange('quantity')} margin="normal" />
                    <Button onClick={handleSave} variant="contained" color="primary" sx={{ mt: 2 }}>
                        Save Product
                    </Button>
                </Box>
            </Modal>
        </>
    );
};

export default AddProductModal;
