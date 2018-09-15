import h3p2_dp_cehaith2 as dp
import h3p2_memoized_cehaith2 as mem 
import h3p2_recursive_cehaith2 as rec
import time 

# Import image making stuff
import matplotlib.pyplot as plot
from matplotlib.ticker import MaxNLocator   # Plot ticks on integers only
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def main():
    # Comparing all 3 as best as possible
    plot_all_linear()

def plot_all_linear():
    print 'Getting data for linear growth...'
    linear_dp_results = linear_dp(20)
    print 'Finished DP'
    linear_rec_results = linear_rec(20)
    print 'Finished Rec'
    linear_mem_results = linear_mem(20)
    print 'Finished Mem and Done'

    # Generate axes
    x_axis = xrange(20)
    x_label = 'Chain Length'
    y_dp_ops = [res['min_ops'] for res in linear_dp_results]
    y_rec_ops = [res['min_ops'] for res in linear_rec_results]
    y_mem_ops = [res['min_ops'] for res in linear_mem_results]
    y_ops_label = 'Minimum Multiplications'
    y_dp_calls = [res['rec_calls'] for res in linear_dp_results]
    y_rec_calls = [res['rec_calls'] for res in linear_rec_results]
    y_mem_calls = [res['rec_calls'] for res in linear_mem_results]
    y_calls_label = 'Recursive Call Count'
    y_dp_time = [res['time'] for res in linear_dp_results]
    y_rec_time = [res['time'] for res in linear_rec_results]
    y_mem_time = [res['time'] for res in linear_mem_results]
    y_time_label = 'Time to completion (secs)'

    ops_plot_title = 'Minimum Multiplications for Linear Growth of all Algorithms'
    ops_plot_fname = 'min-ops-lin-all'
    calls_plot_title = 'Recusion Call Count for Linear Growth of all Algorithms'
    calls_plot_fname = 'rec-call-lin-all'
    time_plot_title = 'Time to Completion for Linear Growth of all Algorithms'
    time_plot_fname = 'time-lin-all'

    legends = ['Recursion', 'Dynamic Programming', 'Memoized']
    
    make_plot(x_axis, [y_rec_ops, y_dp_ops, y_mem_ops], ops_plot_title, x_label, 
            y_ops_label, legends, ops_plot_fname)
    make_plot(x_axis, [y_rec_calls, y_dp_calls, y_mem_calls], calls_plot_title, 
            x_label, y_calls_label, legends, calls_plot_fname)
    make_plot(x_axis, [y_rec_time, y_dp_time, y_mem_time], time_plot_title, 
            x_label, y_time_label, legends, time_plot_fname)
    

def plot_all_linear_multiples():
    print 'Getting data for linear growth...'
    linear_dp_mult_results = linear_dp_multiples(100, 100)
    print 'Finished DP'
    linear_mem_mult_results = linear_mem_multiples(100, 100)
    print 'Finished Mem and Done'

    # Generate axes
    x_axis = xrange(100 * 100)
    x_label = 'Chain Length'
    y_dp_ops = [res['min_ops'] for res in linear_dp_mult_results]
    y_mem_ops = [res['min_ops'] for res in linear_mem_mult_results]
    y_ops_label = 'Minimum Multiplications'
    y_dp_calls = [res['rec_calls'] for res in linear_dp_mult_results]
    y_mem_calls = [res['rec_calls'] for res in linear_mem_mult_results]
    y_calls_label = 'Recursive Call Count'
    y_dp_time = [res['time'] for res in linear_dp_results]
    y_mem_time = [res['time'] for res in linear_mem_mult_results]
    y_time_label = 'Time to completion (secs)'

    ops_plot_title = 'Minimum Multiplications of Dyn. Prog. and Memoized Algorithms'
    ops_plot_fname = 'min-ops-lin-mult'
    calls_plot_title = 'Recusion Call Count of Dyn. Prog. and Memoized Algorithms'
    calls_plot_fname = 'rec-call-lin-mult'
    time_plot_title = 'Time to Completion of Dyn. Prog. and Memoized Algorithms'
    time_plot_fname = 'time-lin-mult'

    legends = ['Dynamic Programming', 'Memoized']
    
    make_plot(x_axis, [y_dp_ops, y_mem_ops], ops_plot_title, x_label, 
            y_ops_label, legends, ops_plot_fname)
    make_plot(x_axis, [y_rec_calls, y_dp_calls, y_mem_calls], calls_plot_title, 
            x_label, y_calls_label, legends, calls_plot_fname)
    make_plot(x_axis, [y_rec_time, y_dp_time, y_mem_time], time_plot_title, 
            x_label, y_time_label, legends, time_plot_fname)
    
def plot_all_quadratic():
    print 'Getting data for quadratic growth...'
    quad_dp_results = quadratic_dp(20)
    print 'Finished DP'
    quad_mem_results = quadratic_mem(20)
    print 'Finished Mem and Done'

    # Generate axes
    x_axis = xrange(20)
    x_label = 'Chain Length'
    y_dp_ops = [res['min_ops'] for res in quad_dp_results]
    y_mem_ops = [res['min_ops'] for res in quad_mem_results]
    y_ops_label = 'Minimum Multiplications'
    y_dp_calls = [res['fvec_calls'] for res in quad_dp_results]
    y_mem_calls = [res['rec_calls'] for res in quad_mem_results]
    y_calls_label = 'Recursive Call Count'
    y_dp_time = [res['time'] for res in quad_dp_results]
    y_mem_time = [res['time'] for res in quad_mem_results]
    y_time_label = 'Time to completion (secs)'

    ops_plot_title = 'Minimum Multiplications of Dyn. Prog. and Memoized Algorithms'
    ops_plot_fname = 'min-ops-lin-quad'
    calls_plot_title = 'Recusion Call Count of Dyn. Prog. and Memoized Algorithms'
    calls_plot_fname = 'rec-call-lin-quad'
    time_plot_title = 'Time to Completion of Dyn. Prog. and Memoized Algorithms'
    time_plot_fname = 'time-lin-quad'

    legends = ['Dynamic Programming', 'Memoized']
    
    make_plot(x_axis, [y_dp_ops, y_mem_ops], ops_plot_title, x_label, 
            y_ops_label, legends, ops_plot_fname)
    make_plot(x_axis, [y_dp_calls, y_mem_calls], calls_plot_title, 
            x_label, y_calls_label, legends, calls_plot_fname)
    make_plot(x_axis, [y_dp_time, y_mem_time], time_plot_title, 
            x_label, y_time_label, legends, time_plot_fname)

def linear_dp_multiples(n, m):
    results = []
    for i in range(1, n + 1):
        start_t = time.time()
        min_ops = dp.matrix_chain_order([2] * ((i * m) + 1))
        delta_t = time.time() - start_t
        results.append({'time': delta_t, 'rec_calls': 0, 'min_ops': min_ops})
    return results

def linear_mem_multiples(n, m):
    results = []
    for i in range(1, n + 1):
        start_t = time.time()
        min_ops = mem.memoized_matrix_chain([2] * ((i * m) + 1))
        delta_t = time.time() - start_t
        results.append({'time': delta_t, 'rec_calls': mem.rec_calls, 
            'min_ops': min_ops})
        mem.rec_calls = 0
    return results

def linear_dp(n):
    results = []
    for i in range(1, n + 1):
        start_t = time.time()
        min_ops = dp.matrix_chain_order([2] * (i + 1))
        delta_t = time.time() - start_t
        results.append({'time': delta_t, 'rec_calls': 0, 'min_ops': min_ops})
    return results

def linear_rec(n):
    if n > 20:
        print ('WARNING: running the recursive algorithm on even medium sized' +
                'input will take an extremely long time!')
    results = []
    for i in range(1, n + 1):
        start_t = time.time()
        min_ops = rec.recursive_matrix_chain([2] * (i + 1), 1, i)
        delta_t = time.time() - start_t
        results.append({'time': delta_t, 'rec_calls': rec.rec_calls, 
            'min_ops': min_ops})
        rec.rec_calls = 0
    return results

def linear_mem(n):
    results = []
    for i in range(1, n + 1):
        start_t = time.time()
        min_ops = mem.memoized_matrix_chain([2] * (i + 1))
        delta_t = time.time() - start_t
        results.append({'time': delta_t, 'rec_calls': mem.rec_calls, 
            'min_ops': min_ops})
        mem.rec_calls = 0
    return results

def quadratic_dp(n):
    results = []
    for i in range(1, n + 1):
        start_t = time.time()
        min_ops = dp.matrix_chain_order([2] * ((i ** 2) + 1))
        delta_t = time.time() - start_t
        results.append({'time': delta_t, 'rec_calls': 0, 'min_ops': min_ops})
        dp.mult_count = 0
    return results

def quadratic_mem(n):
    if n > 15: 
        print 'WARNING: memoized algorithm will fail if the length is too large!'
    results = []
    for i in range(1, n + 1):
        start_t = time.time()
        min_ops = mem.memoized_matrix_chain([2] * ((i ** 2) + 1))
        delta_t = time.time() - start_t
        results.append({'time': delta_t, 'rec_calls': mem.rec_calls, 
            'min_ops': min_ops})
        mem.rec_calls = 0
    return results

def make_plot(x_axis, y_axes, title, x_label, y_label, legends, img_name):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.set_title(title)
    for i in range(len(y_axes)):
        ax.plot(x_axis, y_axes[i], label=legends[i])
    ax.grid(True)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend(loc='upper left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    canvas.print_figure(img_name)
