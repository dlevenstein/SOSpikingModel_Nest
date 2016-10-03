void nest::iaf_neuron::update(Time const & origin, const long_t from, const long_t to)
{
  assert(to >= 0 && (delay) from < Scheduler::get_min_delay());
  assert(from < to);

  for ( long_t lag = from ; lag < to ; ++lag )
  {
    if ( r_ == 0 )
    {
      // neuron not refractory
      y3_ = P30_*(y0_ + I_e_) + P31_*y1_ + P32_*y2_ + P33_*y3_;
    }
    else // neuron is absolute refractory
     --r_;

    // alpha shape PSCs
    y2_ = P21_*y1_ + P22_ * y2_;
    y1_ *= P11_;
                                                       // apply spikes delivered in this step
    y1_ += PSCInitialValue_* spikes_.get_value(lag);   // the spikes arriving at T+1 have an
                                                       // immediate effect on the state of the
                                                       // neuron
    // threshold crossing
    if (y3_ >= Theta_)
    {
      r_ = RefractoryCounts_;
      y3_=V_reset_;
      // A supra-threshold membrane potential should never be observable.
      // The reset at the time of threshold crossing enables accurate integration
      // independent of the computation step size, see [2,3] for details.

      set_spiketime(Time::step(origin.get_steps()+lag+1));
      SpikeEvent se;
      network()->send(*this, se, lag);
    }

    // set new input current
    y0_ = currents_.get_value(lag);

    // voltage logging for entire time slice
    potentials_[network()->get_slice() % 2][lag] = y3_ + U0_;
  }
}
