import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [target, setTarget] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleInvestigate = async () => {
    if (!target) return;
    setLoading(true);
    try {
      const response = await axios.get(`http://localhost:8001/investigate?target=${target}`);
      setResults(response.data.results);
    } catch (error) {
      console.error("Investigation failed", error);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-[#020203] text-slate-300 font-mono p-6">
      {/* Header */}
      <div className="max-w-6xl mx-auto flex justify-between items-center mb-12 border-b border-white/5 pb-6">
        <div>
          <h1 className="text-2xl font-black text-cyan-500 tracking-tighter italic">SPY-SOURCE OSINT</h1>
          <p className="text-[10px] text-slate-600 tracking-[0.4em] uppercase">Unified Intelligence Aggregator</p>
        </div>
        <div className="text-right">
          <span className="text-[10px] bg-cyan-500/10 text-cyan-500 px-3 py-1 rounded-full border border-cyan-500/20">AGENT ACTIVE</span>
        </div>
      </div>

      <div className="max-w-6xl mx-auto grid grid-cols-12 gap-8">
        
        {/* Sidebar: Search Control */}
        <div className="col-span-12 lg:col-span-4 space-y-6">
          <div className="bg-white/[0.02] border border-white/10 p-6 rounded-3xl backdrop-blur-xl">
            <label className="text-[10px] font-bold text-slate-500 uppercase mb-4 block tracking-widest">Input Target Identitas</label>
            <input 
              className="w-full bg-black/50 border border-white/10 rounded-xl px-4 py-3 text-sm focus:border-cyan-500 outline-none transition mb-4"
              placeholder="Nama Lengkap / No HP..."
              value={target}
              onChange={(e) => setTarget(e.target.value)}
            />
            <button 
              onClick={handleInvestigate}
              disabled={loading}
              className="w-full bg-cyan-500 hover:bg-cyan-400 text-black font-black py-3 rounded-xl transition transform active:scale-95 disabled:opacity-50"
            >
              {loading ? 'ANALYZING DATA...' : 'START INVESTIGATION'}
            </button>
          </div>

          {results && (
            <div className="bg-cyan-500/5 border border-cyan-500/20 p-6 rounded-3xl">
              <h3 className="text-xs font-bold text-cyan-400 mb-2 uppercase">Analysis Summary</h3>
              <p className="text-[11px] text-slate-400 leading-relaxed">
                Ditemukan {results.dorking.length} dokumen publik terkait di server pemerintah. 
                Sistem mendeteksi potensi jejak digital pada {results.social_media.length} platform.
              </p>
            </div>
          )}
        </div>

        {/* Main Panel: Results */}
        <div className="col-span-12 lg:col-span-8 space-y-6">
          {results ? (
            <>
              {/* Dorking Results */}
              <div className="bg-white/[0.02] border border-white/10 rounded-3xl overflow-hidden">
                <div className="p-4 bg-white/5 border-b border-white/10 flex justify-between items-center">
                  <h3 className="text-[10px] font-bold uppercase tracking-widest text-slate-400">Government & Public Documents (.id)</h3>
                </div>
                <div className="divide-y divide-white/5 max-h-[400px] overflow-y-auto">
                  {results.dorking.map((item, i) => (
                    <div key={i} className="p-4 hover:bg-white/[0.02] transition">
                      <a href={item.link} target="_blank" rel="noreferrer" className="text-cyan-400 text-sm font-bold block mb-1 hover:underline">
                        {item.title}
                      </a>
                      <p className="text-[10px] text-slate-500 leading-relaxed italic">{item.snippet}</p>
                    </div>
                  ))}
                </div>
              </div>

              {/* Social Media Grid */}
              <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                {results.social_media.map((social, i) => (
                  <div key={i} className="bg-white/[0.02] border border-white/10 p-4 rounded-2xl flex items-center justify-between">
                    <span className="text-xs font-bold">{social.platform}</span>
                    <a href={social.link} className="text-[9px] bg-cyan-500 text-black px-2 py-1 rounded font-bold">VIEW</a>
                  </div>
                ))}
              </div>
            </>
          ) : (
            <div className="h-[400px] flex flex-col items-center justify-center border-2 border-dashed border-white/5 rounded-3xl">
              <div className="text-slate-700 text-5xl mb-4 animate-pulse">🔎</div>
              <p className="text-slate-600 text-[11px] uppercase tracking-[0.3em]">Waiting for investigation input...</p>
            </div>
          )}
        </div>

      </div>
    </div>
  );
};

export default App;
