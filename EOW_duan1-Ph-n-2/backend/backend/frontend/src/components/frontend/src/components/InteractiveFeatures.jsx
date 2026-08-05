import React, { useEffect, useState } from 'react';

export default function InteractiveFeatures({ characterId = "quang-trung" }) {
    const [timeline, setTimeline] = useState([]);
    const [gallery, setGallery] = useState([]);

    useEffect(() => {
        // Fetch Timeline
        fetch(`http://localhost:8000/api/timeline/${characterId}`)
            .then(res => res.json())
            .then(data => setTimeline(data));

        // Fetch Gallery
        fetch(`http://localhost:8000/api/gallery/${characterId}`)
            .then(res => res.json())
            .then(data => setGallery(data));
    }, [characterId]);

    return (
        <div className="max-w-lg mx-auto text-white mt-6 space-y-6">
            {/* Timeline Component */}
            <div className="bg-slate-900 p-4 rounded-xl border border-slate-800">
                <h3 className="text-md font-bold mb-3 text-amber-500">Dòng Thời Gian Lịch Sử</h3>
                <div className="border-l-2 border-amber-600 pl-4 space-y-3">
                    {timeline.map((item, idx) => (
                        <div key={idx}>
                            <span className="text-xs font-bold text-amber-400">{item.year}</span>
                            <h4 className="text-sm font-semibold">{item.title}</h4>
                            <p className="text-xs text-slate-400">{item.description}</p>
                        </div>
                    ))}
                </div>
            </div>

            {/* Gallery Component */}
            <div className="bg-slate-900 p-4 rounded-xl border border-slate-800">
                <h3 className="text-md font-bold mb-3 text-amber-500">Thư Viện Ảnh Tư Liệu</h3>
                <div className="grid grid-cols-2 gap-3">
                    {gallery.map((item) => (
                        <div key={item.id} className="bg-slate-800 p-2 rounded-lg text-center">
                            <img src={item.image_url} alt={item.title} className="w-full h-24 object-cover rounded mb-2" />
                            <p className="text-xs text-slate-300">{item.title}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}