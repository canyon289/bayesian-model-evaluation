var margin = {top: 20, right: 10, bottom: 50, left: 10},
    width = 850 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

function randomProperty(obj) {
    var keys = Object.keys(obj);
    var key = keys[ keys.length * Math.random() << 0];
    return [key, obj[key]];
};

function randomFunction() {
  var fn = randomProperty({
          "1 - 0.2 x": function(x){return 1 - 0.2 * x},
          "x^2": function(x){return x * x},
          "\\sin{(5x)}": function(x){return Math.sin(5 * x)},
          "\\cos{(5x)}": function(x){return Math.cos(5 * x)},
          "|\\cos{(5x)}|": function(x){return Math.abs(Math.cos(5 * x))},
          "e^x": function(x){return Math.exp(x)},
          "\\frac{1}{1 + e^{-9x}}": function(x){ return 1.0 / (1 + Math.exp(-9 * x))},
          "\\sin{\\frac{1}{x}}": function(x) { return Math.sin(1.0 / x)}
  })

  var trainingPoints = 10 + Math.abs(Math.round(Math.random() * 200)),
      x = d3.range(trainingPoints)
            .map(d3.randomUniform(-1, 1))
            .sort(function (a, b) { return a - b }),
      y = x.map(fn[1]),
      noise = 0.3 * Math.abs(Math.random()),
      random = d3.randomNormal(0, noise),
      yNoise = y.map(function(d) { return d + random(); });

  return {
    trainingPoints: trainingPoints,
    x: x,
    y: y,
    yNoise: yNoise,
    name: fn[0],
    fn: fn[1],
    noise: noise,
    };
}

function update(svg) {
  var fn = randomFunction();
  if (typeof svg !== undefined) {
    updatePlot(fn, svg);
  }
}

function drawPlot() {
  return d3.select('#graph').append("svg")
              .attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom)
              .append("g")
              .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
}

function getExtent(ary) {
  var extent = d3.extent(ary),
      range = extent[1] - extent[0];
  return [extent[0] - 0.05 * range, extent[1] + 0.05 * range];
}

function updatePlot(fn, svg) {
  var x = d3.scaleLinear()
            .range([0, width])
            .domain(getExtent(fn.x)),
      y = d3.scaleLinear()
            .range([height, 0])
            .domain(getExtent(fn.yNoise));

  var data = d3.zip(fn.x, fn.y, fn.yNoise).map(function(d) {
      return { x: d[0], y: d[1], yNoise: d[2] };
    })

  var points = svg.selectAll(".dot")
                  .data(data);

  points.enter()
      .append("circle")
      .attr("class", "dot")
      .attr("opacity", 0.0)
      .attr("r", 10)
      .attr("cx", function(d) { return x(d.x);})
      .attr("cy", function(d) { return y(d.y);})
      .transition()
      .duration(500)
      .attr("opacity", 0.8)
      .transition()
      .duration(500)
      .attr("cy", function(d) { return y(d.yNoise);});

  points.transition()
        .duration(500)
        .attr("cx", function(d) { return x(d.x);})
        .attr("cy", function(d) { return y(d.y);})
        .transition()
        .duration(500)
        .attr("cy", function(d) { return y(d.yNoise);});

  points.exit()
        .transition()
        .duration(500)
        .attr("opacity", 0.0)
        .remove();
}

var updater;

function startUpdater(svg) {
  updater = setInterval(function() { return update(svg); }, 3000);
}

function stopUpdater() {
  window.clearInterval(updater);
}

$(document).ready(function() {
  var svg = drawPlot();
  update(svg);
  startUpdater(svg);
  window.addEventListener('focus', function() { update(svg); startUpdater(svg); });
  window.addEventListener('blur', stopUpdater);
});
