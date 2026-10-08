import React, { useState, useEffect } from 'react';
import { procurementService } from '../../services/procurementService';
import { inventoryApi } from '../../api/inventoryApi';
import { useNotification } from '../../context/NotificationContext';
import { formatCurrency } from '../../utils/constants';
import Modal from '../../components/common/Modal';
import {
  Truck,
  Plus,
  RefreshCw,
  Package,
  Building,
  CheckCircle2,
  Clock,
  ArrowRight,
  Receipt,
  Boxes,
} from 'lucide-react';

export const ProcurementPage = () => {
  const { showSuccess, showError } = useNotification();
  const [activeTab, setActiveTab] = useState('orders'); // 'orders' | 'suppliers'
  const [suppliers, setSuppliers] = useState([]);
  const [orders, setOrders] = useState([]);
  const [products, setProducts] = useState([]);
  const [warehouses, setWarehouses] = useState([]);
  const [loading, setLoading] = useState(true);

  // Modals
  const [supplierModalOpen, setSupplierModalOpen] = useState(false);
  const [orderModalOpen, setOrderModalOpen] = useState(false);
  const [receiveModalOpen, setReceiveModalOpen] = useState(false);
  const [selectedOrder, setSelectedOrder] = useState(null);
  const [submitting, setSubmitting] = useState(false);

  // Form states
  const [supplierForm, setSupplierForm] = useState({
    name: '',
    contact_person: '',
    email: '',
    phone: '',
    address: '',
    tax_id: '',
  });

  const [orderForm, setOrderForm] = useState({
    supplier_id: '',
    warehouse_id: '',
    notes: '',
    items: [{ product_id: '', quantity: 1, unit_price: 0 }],
  });

  const [receiveWarehouseId, setReceiveWarehouseId] = useState('');

  const fetchData = async () => {
    setLoading(true);
    try {
      const [supRes, ordRes] = await Promise.all([
        procurementService.getSuppliers(),
        procurementService.getPurchaseOrders(),
      ]);
      setSuppliers(supRes);
      setOrders(ordRes);

      // fetch products and warehouses for order creation
      try {
        const pRes = await inventoryApi.getProducts({ page_size: 100 });
        setProducts(pRes.items || []);
        const wRes = await inventoryApi.getWarehouses();
        setWarehouses(wRes || []);
      } catch (e) {
        // inventory might be empty or fallback
      }
    } catch (err) {
      showError('Failed to load procurement records');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleCreateSupplier = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await procurementService.createSupplier(supplierForm);
      showSuccess('Vendor supplier registered successfully');
      setSupplierModalOpen(false);
      setSupplierForm({ name: '', contact_person: '', email: '', phone: '', address: '', tax_id: '' });
      fetchData();
    } catch (err) {
      showError(err.response?.data?.detail || 'Failed to create supplier');
    } finally {
      setSubmitting(false);
    }
  };

  const handleAddItemRow = () => {
    setOrderForm({
      ...orderForm,
      items: [...orderForm.items, { product_id: '', quantity: 1, unit_price: 0 }],
    });
  };

  const handleRemoveItemRow = (idx) => {
    const updated = [...orderForm.items];
    updated.splice(idx, 1);
    setOrderForm({ ...orderForm, items: updated });
  };

  const handleItemChange = (idx, field, val) => {
    const updated = [...orderForm.items];
    updated[idx][field] = val;

    // auto populate unit price if product selected
    if (field === 'product_id') {
      const prod = products.find((p) => p.id === parseInt(val, 10));
      if (prod) {
        updated[idx].unit_price = parseFloat(prod.cost_price || 0);
      }
    }

    setOrderForm({ ...orderForm, items: updated });
  };

  const handleCreateOrder = async (e) => {
    e.preventDefault();
    if (!orderForm.supplier_id) {
      showError('Please select a supplier');
      return;
    }
    if (orderForm.items.length === 0 || !orderForm.items[0].product_id) {
      showError('Please add at least one valid product item');
      return;
    }

    setSubmitting(true);
    try {
      await procurementService.createPurchaseOrder({
        supplier_id: parseInt(orderForm.supplier_id, 10),
        warehouse_id: orderForm.warehouse_id ? parseInt(orderForm.warehouse_id, 10) : null,
        notes: orderForm.notes,
        items: orderForm.items.map((it) => ({
          product_id: parseInt(it.product_id, 10),
          quantity: parseInt(it.quantity, 10) || 1,
          unit_price: parseFloat(it.unit_price, 10) || 0,
        })),
      });
      showSuccess('Purchase order generated successfully');
      setOrderModalOpen(false);
      setOrderForm({
        supplier_id: '',
        warehouse_id: '',
        notes: '',
        items: [{ product_id: '', quantity: 1, unit_price: 0 }],
      });
      fetchData();
    } catch (err) {
      showError(err.response?.data?.detail || 'Failed to create purchase order');
    } finally {
      setSubmitting(false);
    }
  };

  const handleReceiveGoods = async () => {
    if (!selectedOrder) return;
    setSubmitting(true);
    try {
      await procurementService.receiveGoods(selectedOrder.id, {
        warehouse_id: receiveWarehouseId ? parseInt(receiveWarehouseId, 10) : undefined,
      });
      showSuccess(`Goods receipt confirmed! Inventory updated for PO #${selectedOrder.order_number}`);
      setReceiveModalOpen(false);
      setSelectedOrder(null);
      fetchData();
    } catch (err) {
      showError(err.response?.data?.detail || 'Failed to receive goods');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      {/* Title & Actions */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight">Procurement & Suppliers</h1>
          <p className="text-xs text-slate-400 mt-1">
            Vendor relationship management, inbound purchase orders, and goods receipt notes (GRN).
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={fetchData}
            className="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors"
            title="Refresh Procurement"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
          </button>
          <button
            onClick={() => setSupplierModalOpen(true)}
            className="px-4 py-2.5 rounded-xl text-xs font-semibold text-slate-200 bg-slate-800 hover:bg-slate-700 border border-slate-700 transition-all flex items-center gap-1.5"
          >
            <Building className="w-4 h-4" />
            <span>Add Supplier</span>
          </button>
          <button
            onClick={() => setOrderModalOpen(true)}
            className="px-4 py-2.5 rounded-xl text-xs font-semibold text-white bg-amber-600 hover:bg-amber-500 shadow-lg shadow-amber-600/30 transition-all flex items-center gap-1.5"
          >
            <Plus className="w-4 h-4" />
            <span>New Purchase Order</span>
          </button>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex border-b border-slate-800 space-x-6 text-xs">
        <button
          onClick={() => setActiveTab('orders')}
          className={`pb-3 font-semibold transition-colors relative ${
            activeTab === 'orders' ? 'text-amber-400 border-b-2 border-amber-400' : 'text-slate-400 hover:text-white'
          }`}
        >
          Purchase Orders ({orders.length})
        </button>
        <button
          onClick={() => setActiveTab('suppliers')}
          className={`pb-3 font-semibold transition-colors relative ${
            activeTab === 'suppliers' ? 'text-amber-400 border-b-2 border-amber-400' : 'text-slate-400 hover:text-white'
          }`}
        >
          Approved Suppliers ({suppliers.length})
        </button>
      </div>

      {/* Purchase Orders View */}
      {activeTab === 'orders' && (
        <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-900/80 border-b border-slate-800 text-slate-400 font-semibold">
                <tr>
                  <th className="p-4">PO Number</th>
                  <th className="p-4">Supplier</th>
                  <th className="p-4">Order Date</th>
                  <th className="p-4">Items Count</th>
                  <th className="p-4">Total Amount</th>
                  <th className="p-4">Status</th>
                  <th className="p-4 text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {orders.length === 0 ? (
                  <tr>
                    <td colSpan="7" className="py-8 text-center text-slate-500">
                      No purchase orders issued yet.
                    </td>
                  </tr>
                ) : (
                  orders.map((po) => (
                    <tr key={po.id} className="hover:bg-slate-800/40 transition-colors">
                      <td className="p-4 font-mono font-semibold text-amber-400">{po.order_number}</td>
                      <td className="p-4 font-semibold text-white">{po.supplier_name || 'Vendor'}</td>
                      <td className="p-4 text-slate-400">{new Date(po.order_date).toLocaleDateString()}</td>
                      <td className="p-4 text-slate-300 font-mono">{po.items?.length || 0} line items</td>
                      <td className="p-4 font-mono font-semibold text-slate-200">
                        {formatCurrency(po.total_amount)}
                      </td>
                      <td className="p-4">
                        <span
                          className={`text-[10px] px-2 py-0.5 rounded-full font-bold uppercase border ${
                            po.status === 'Received'
                              ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20'
                              : 'bg-amber-500/10 text-amber-400 border-amber-500/20'
                          }`}
                        >
                          {po.status}
                        </span>
                      </td>
                      <td className="p-4 text-right">
                        {po.status !== 'Received' ? (
                          <button
                            onClick={() => {
                              setSelectedOrder(po);
                              setReceiveWarehouseId(po.warehouse_id || '');
                              setReceiveModalOpen(true);
                            }}
                            className="px-2.5 py-1 rounded-lg bg-emerald-600/20 hover:bg-emerald-600 text-emerald-300 hover:text-white text-[11px] font-semibold border border-emerald-500/30 transition-all"
                          >
                            <Boxes className="w-3.5 h-3.5 inline mr-1" />
                            Receive Stock
                          </button>
                        ) : (
                          <span className="text-slate-500 text-[11px] flex items-center justify-end gap-1">
                            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                            Inventory Received
                          </span>
                        )}
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Suppliers View */}
      {activeTab === 'suppliers' && (
        <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-900/80 border-b border-slate-800 text-slate-400 font-semibold">
                <tr>
                  <th className="p-4">Supplier Name</th>
                  <th className="p-4">Contact Person</th>
                  <th className="p-4">Email</th>
                  <th className="p-4">Phone</th>
                  <th className="p-4">GST / Tax ID</th>
                  <th className="p-4">City / Address</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {suppliers.length === 0 ? (
                  <tr>
                    <td colSpan="6" className="py-8 text-center text-slate-500">
                      No suppliers registered yet.
                    </td>
                  </tr>
                ) : (
                  suppliers.map((sup) => (
                    <tr key={sup.id} className="hover:bg-slate-800/40 transition-colors">
                      <td className="p-4 font-semibold text-white">{sup.name}</td>
                      <td className="p-4 text-slate-300">{sup.contact_person || '—'}</td>
                      <td className="p-4 text-slate-400">{sup.email || '—'}</td>
                      <td className="p-4 text-slate-400">{sup.phone || '—'}</td>
                      <td className="p-4 font-mono text-slate-300">{sup.tax_id || '—'}</td>
                      <td className="p-4 text-slate-400">{sup.address || '—'}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Add Supplier Modal */}
      <Modal isOpen={supplierModalOpen} onClose={() => setSupplierModalOpen(false)} title="Register Supplier Vendor">
        <form onSubmit={handleCreateSupplier} className="space-y-4 text-xs">
          <div>
            <label className="block text-slate-400 mb-1 font-medium">Vendor / Supplier Name *</label>
            <input
              required
              type="text"
              value={supplierForm.name}
              onChange={(e) => setSupplierForm({ ...supplierForm, name: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-amber-500"
            />
          </div>
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Contact Person</label>
              <input
                type="text"
                value={supplierForm.contact_person}
                onChange={(e) => setSupplierForm({ ...supplierForm, contact_person: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-amber-500"
              />
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Tax ID / GST</label>
              <input
                type="text"
                value={supplierForm.tax_id}
                onChange={(e) => setSupplierForm({ ...supplierForm, tax_id: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-amber-500"
              />
            </div>
          </div>
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Email</label>
              <input
                type="email"
                value={supplierForm.email}
                onChange={(e) => setSupplierForm({ ...supplierForm, email: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-amber-500"
              />
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Phone</label>
              <input
                type="text"
                value={supplierForm.phone}
                onChange={(e) => setSupplierForm({ ...supplierForm, phone: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-amber-500"
              />
            </div>
          </div>
          <div>
            <label className="block text-slate-400 mb-1 font-medium">Address</label>
            <textarea
              rows="2"
              value={supplierForm.address}
              onChange={(e) => setSupplierForm({ ...supplierForm, address: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-amber-500"
            />
          </div>
          <div className="flex justify-end gap-3 pt-3 border-t border-slate-800">
            <button
              type="button"
              onClick={() => setSupplierModalOpen(false)}
              className="px-4 py-2 rounded-xl text-slate-400 hover:text-white bg-slate-800"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={submitting}
              className="px-4 py-2 rounded-xl text-white font-semibold bg-amber-600 hover:bg-amber-500"
            >
              {submitting ? 'Saving...' : 'Add Supplier'}
            </button>
          </div>
        </form>
      </Modal>

      {/* New Purchase Order Modal */}
      <Modal isOpen={orderModalOpen} onClose={() => setOrderModalOpen(false)} title="Generate Purchase Order">
        <form onSubmit={handleCreateOrder} className="space-y-4 text-xs max-h-[70vh] overflow-y-auto">
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Supplier *</label>
              <select
                required
                value={orderForm.supplier_id}
                onChange={(e) => setOrderForm({ ...orderForm, supplier_id: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-amber-500"
              >
                <option value="">Select Vendor</option>
                {suppliers.map((s) => (
                  <option key={s.id} value={s.id}>
                    {s.name}
                  </option>
                ))}
              </select>
            </div>
            <div>
              <label className="block text-slate-400 mb-1 font-medium">Destination Warehouse</label>
              <select
                value={orderForm.warehouse_id}
                onChange={(e) => setOrderForm({ ...orderForm, warehouse_id: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-amber-500"
              >
                <option value="">Default Warehouse</option>
                {warehouses.map((w) => (
                  <option key={w.id} value={w.id}>
                    {w.warehouse_name}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="text-slate-400 font-medium">Purchase Order Line Items *</label>
              <button
                type="button"
                onClick={handleAddItemRow}
                className="text-[11px] text-amber-400 hover:text-amber-300 font-semibold"
              >
                + Add Product
              </button>
            </div>

            <div className="space-y-2">
              {orderForm.items.map((it, idx) => (
                <div key={idx} className="flex items-center gap-2 bg-slate-950 p-2 rounded-xl border border-slate-800">
                  <select
                    required
                    value={it.product_id}
                    onChange={(e) => handleItemChange(idx, 'product_id', e.target.value)}
                    className="flex-1 bg-slate-900 border border-slate-800 rounded-lg p-2 text-white"
                  >
                    <option value="">Select Product Catalog Item</option>
                    {products.map((p) => (
                      <option key={p.id} value={p.id}>
                        {p.product_name} ({p.sku})
                      </option>
                    ))}
                  </select>

                  <input
                    type="number"
                    min="1"
                    placeholder="Qty"
                    value={it.quantity}
                    onChange={(e) => handleItemChange(idx, 'quantity', e.target.value)}
                    className="w-20 bg-slate-900 border border-slate-800 rounded-lg p-2 text-white text-center"
                  />

                  <input
                    type="number"
                    step="0.01"
                    placeholder="Unit Price"
                    value={it.unit_price}
                    onChange={(e) => handleItemChange(idx, 'unit_price', e.target.value)}
                    className="w-24 bg-slate-900 border border-slate-800 rounded-lg p-2 text-white text-right"
                  />

                  {orderForm.items.length > 1 && (
                    <button
                      type="button"
                      onClick={() => handleRemoveItemRow(idx)}
                      className="text-rose-400 p-1 hover:text-rose-300"
                    >
                      ✕
                    </button>
                  )}
                </div>
              ))}
            </div>
          </div>

          <div>
            <label className="block text-slate-400 mb-1 font-medium">Notes / Terms</label>
            <textarea
              rows="2"
              value={orderForm.notes}
              onChange={(e) => setOrderForm({ ...orderForm, notes: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-amber-500"
            />
          </div>

          <div className="flex justify-end gap-3 pt-3 border-t border-slate-800">
            <button
              type="button"
              onClick={() => setOrderModalOpen(false)}
              className="px-4 py-2 rounded-xl text-slate-400 hover:text-white bg-slate-800"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={submitting}
              className="px-4 py-2 rounded-xl text-white font-semibold bg-amber-600 hover:bg-amber-500"
            >
              {submitting ? 'Generating...' : 'Issue Purchase Order'}
            </button>
          </div>
        </form>
      </Modal>

      {/* Receive Goods Confirmation Modal */}
      <Modal isOpen={receiveModalOpen} onClose={() => setReceiveModalOpen(false)} title="Receive Inbound Goods (GRN)">
        <div className="space-y-4 text-xs">
          <p className="text-slate-300">
            Confirm receipt of items for Purchase Order <span className="font-mono font-bold text-amber-400">{selectedOrder?.order_number}</span>?
          </p>
          <div>
            <label className="block text-slate-400 mb-1 font-medium">Receiving Warehouse</label>
            <select
              value={receiveWarehouseId}
              onChange={(e) => setReceiveWarehouseId(e.target.value)}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:outline-none focus:border-emerald-500"
            >
              <option value="">Default Warehouse</option>
              {warehouses.map((w) => (
                <option key={w.id} value={w.id}>
                  {w.warehouse_name}
                </option>
              ))}
            </select>
          </div>
          <div className="p-3 rounded-xl bg-emerald-950/20 border border-emerald-500/30 text-emerald-300 space-y-1">
            <div className="font-semibold flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4" />
              Automated Stock Integration
            </div>
            <div className="text-[11px] opacity-90">
              The quantities in this purchase order will immediately increment product inventory levels in the selected warehouse.
            </div>
          </div>
          <div className="flex justify-end gap-3 pt-2">
            <button
              type="button"
              onClick={() => setReceiveModalOpen(false)}
              className="px-4 py-2 rounded-xl text-slate-400 hover:text-white bg-slate-800"
            >
              Cancel
            </button>
            <button
              type="button"
              disabled={submitting}
              onClick={handleReceiveGoods}
              className="px-4 py-2 rounded-xl text-white font-semibold bg-emerald-600 hover:bg-emerald-500"
            >
              {submitting ? 'Receiving...' : 'Confirm Stock Receipt'}
            </button>
          </div>
        </div>
      </Modal>
    </div>
  );
};

export default ProcurementPage;
