import React, { useState } from 'react';

export default function AdminCMS() {
  const [formData, setFormData] = useState({
    title: '',
    character_code: 'dang_thuy_tram',
    time_period: '',
    location: '',
    tags: ''
  });
  const [file, setFile] = useState(null);
  const [statusMsg, setStatusMsg] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert('Vui lòng chọn một file tài liệu (PDF, DOCX, TXT)!');
      return;
    }

    setLoading(true);
    setStatusMsg('Đang xử lý trích xuất văn bản, làm sạch & nạp vào Vector Database...');

    // Đóng gói dữ liệu dạng Multipart Form-Data để gửi kèm File
    const bodyData = new FormData();
    bodyData.append('title', formData.title);
    bodyData.append('character_code', formData.character_code);
    bodyData.append('time_period', formData.time_period);
    bodyData.append('location', formData.location);
    bodyData.append('tags', formData.tags);
    bodyData.append('file', file);

    try {
            // Sửa dòng fetch trong hàm handleSubmit:
        const response = await fetch('http://127.0.0.1:8000/api/admin/knowledge/upload', {
        method: 'POST',
        body: bodyData,
        });

      const result = await response.json();

      if (response.ok) {
        setStatusMsg(`✅ THÀNH CÔNG: ${result.message || 'Đã nạp dữ liệu thành công!'} (Tổng số chunk đã index: ${result.total_chunks})`);
        // Reset file input sau khi upload thành công
        setFile(null);
      } else {
        setStatusMsg(`❌ LỖI: ${result.detail || 'Không thể xử lý tài liệu.'}`);
      }
    } catch (error) {
      console.error(error);
      setStatusMsg('❌ LỖI: Không thể kết nối tới máy chủ Backend (127.0.0.1:8000).');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      maxWidth: '700px',
      margin: '40px auto',
      padding: '30px',
      backgroundColor: '#1e1e1e',
      borderRadius: '8px',
      color: '#ffffff',
      boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
      fontFamily: 'sans-serif'
    }}>
      <h2 style={{ borderBottom: '2px solid #333', paddingBottom: '10px', marginTop: 0 }}>
        📚 Quản Trị Tri Thức Lịch Sử (Admin CMS)
      </h2>
      <p style={{ color: '#aaa', fontSize: '0.9rem' }}>
        Tải lên tài liệu, trích xuất text, gán Metadata và đồng bộ tự động vào Vector Database (ChromaDB).
      </p>

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px', marginTop: '20px' }}>
        <div>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Tiêu đề tài liệu / Hồ sơ (*):</label>
          <input 
            type="text" 
            required 
            placeholder="Ví dụ: Nhật ký Đặng Thùy Trâm - Tập 1"
            value={formData.title}
            onChange={e => setFormData({ ...formData, title: e.target.value })} 
            style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #444', background: '#2a2a2a', color: '#fff', boxSizing: 'border-box' }} 
          />
        </div>

        <div>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Gán Nhân vật lịch sử (*):</label>
          <select 
            value={formData.character_code}
            onChange={e => setFormData({ ...formData, character_code: e.target.value })}
            style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #444', background: '#2a2a2a', color: '#fff', boxSizing: 'border-box' }}
          >
            <option value="dang_thuy_tram">🩺 Bác sĩ Đặng Thùy Trâm</option>
            <option value="linh_giai_phong">🎖️ Anh lính Giải phóng quân</option>
            <option value="em_be_thoi_chien">🎒 Em bé thời chiến (1972)</option>
          </select>
        </div>

        <div style={{ display: 'flex', gap: '15px' }}>
          <div style={{ flex: 1 }}>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Thời gian (Metadata):</label>
            <input 
              type="text" 
              placeholder="Vd: 1968-1970" 
              value={formData.time_period}
              onChange={e => setFormData({ ...formData, time_period: e.target.value })}
              style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #444', background: '#2a2a2a', color: '#fff', boxSizing: 'border-box' }} 
            />
          </div>
          <div style={{ flex: 1 }}>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Địa điểm (Metadata):</label>
            <input 
              type="text" 
              placeholder="Vd: Quảng Ngãi" 
              value={formData.location}
              onChange={e => setFormData({ ...formData, location: e.target.value })}
              style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #444', background: '#2a2a2a', color: '#fff', boxSizing: 'border-box' }} 
            />
          </div>
        </div>

        <div>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Thẻ phân loại / Tags (Metadata):</label>
          <input 
            type="text" 
            placeholder="Vd: nhat_ky, y_te, chiến_trường (phân cách bằng dấu phẩy)" 
            value={formData.tags}
            onChange={e => setFormData({ ...formData, tags: e.target.value })}
            style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #444', background: '#2a2a2a', color: '#fff', boxSizing: 'border-box' }} 
          />
        </div>

        <div>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Chọn File văn bản (PDF, DOCX, TXT) (*):</label>
          <input 
            type="file" 
            accept=".pdf,.docx,.doc,.txt" 
            onChange={e => setFile(e.target.files[0])} 
            style={{ color: '#ccc', padding: '5px 0' }} 
          />
        </div>

        <button 
          type="submit" 
          disabled={loading}
          style={{
            padding: '12px',
            backgroundColor: loading ? '#666' : '#28a745',
            color: '#fff',
            border: 'none',
            borderRadius: '4px',
            fontWeight: 'bold',
            fontSize: '1rem',
            cursor: loading ? 'not-allowed' : 'pointer',
            marginTop: '10px'
          }}
        >
          {loading ? 'Đang Xử Lý & Index...' : '🚀 Tải Lên & Đồng Bộ Vào Vector DB'}
        </button>
      </form>

      {statusMsg && (
        <div style={{
          marginTop: '20px',
          padding: '12px',
          backgroundColor: '#2a2a2a',
          borderRadius: '4px',
          borderLeft: '4px solid #007bff',
          fontSize: '0.95rem',
          lineHeight: '1.4'
        }}>
          {statusMsg}
        </div>
      )}
    </div>
  );
}