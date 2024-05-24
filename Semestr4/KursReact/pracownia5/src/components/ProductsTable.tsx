import React, { useState } from 'react';
import {
    Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, TableSortLabel,
    TablePagination, Button, Snackbar, Alert
} from '@mui/material';

import Product from './ProductInterface';

interface ProductTableProps {
    products: Product[];
    onDelete: (id: string) => void;
}

const ProductTable: React.FC<ProductTableProps> = ({ products, onDelete }) => {
    const [order, setOrder] = useState<'asc' | 'desc'>('asc');
    const [orderBy, setOrderBy] = useState<keyof Product>('name');
    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(5);
    const [snackbarOpen, setSnackbarOpen] = useState(false);

    const handleRequestSort = (property: keyof Product) => {
        const isAsc = orderBy === property && order === 'asc';
        setOrder(isAsc ? 'desc' : 'asc');
        setOrderBy(property);
        products.sort((a, b) => {
            if (a[property] < b[property]) {
                return isAsc ? 1 : -1;
            }
            if (a[property] > b[property]) {
                return isAsc ? -1 : 1;
            }
            return 0;
        });
    };

    const handleChangePage = (event: unknown, newPage: number) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
    };

    const confirmDelete = (id: string) => {
        if (window.confirm("Are you sure you want to delete this product?")) {
            onDelete(id);
            setSnackbarOpen(true);
        }
    }

    const handleCloseSnackbar = () => {
        setSnackbarOpen(false);
    };

    return (
        <>
            <TableContainer component={Paper}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>Product Name <TableSortLabel active={orderBy === 'name'} direction={order} onClick={() => handleRequestSort('name')} /></TableCell>
                            <TableCell>Type <TableSortLabel active={orderBy === 'type'} direction={order} onClick={() => handleRequestSort('type')} /></TableCell>
                            <TableCell>Price <TableSortLabel active={orderBy === 'price'} direction={order} onClick={() => handleRequestSort('price')} /></TableCell>
                            <TableCell>Availability <TableSortLabel active={orderBy === 'availability'} direction={order} onClick={() => handleRequestSort('availability')} /></TableCell>
                            <TableCell>Quantity <TableSortLabel active={orderBy === 'quantity'} direction={order} onClick={() => handleRequestSort('quantity')} /></TableCell>
                            <TableCell>Action</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {products.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage).map((product) => (
                            <TableRow key={product.id}>
                                <TableCell>{product.name}</TableCell>
                                <TableCell>{product.type}</TableCell>
                                <TableCell>${product.price.toFixed(2)}</TableCell>
                                <TableCell>{product.availability ? 'Available' : 'Unavailable'}</TableCell>
                                <TableCell>{product.quantity}</TableCell>
                                <TableCell>
                                    <Button variant="outlined" color="error" onClick={() => confirmDelete(product.id)}>
                                        Delete
                                    </Button>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                    <TablePagination
                        rowsPerPageOptions={[5, 10, 25]}
                        component="div"
                        count={products.length}
                        rowsPerPage={rowsPerPage}
                        page={page}
                        onPageChange={handleChangePage}
                        onRowsPerPageChange={handleChangeRowsPerPage}
                    />
                </Table>
            </TableContainer>
            <Snackbar open={snackbarOpen} autoHideDuration={6000} onClose={handleCloseSnackbar} anchorOrigin={{ vertical: 'bottom', horizontal: 'left' }}>
                <Alert onClose={handleCloseSnackbar} severity="success" sx={{ width: '100%' }}>
                    Product removed successfully!
                </Alert>
            </Snackbar>
        </>
    );
};

export default ProductTable;
