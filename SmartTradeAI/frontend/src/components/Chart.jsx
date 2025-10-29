import React, { useRef, useEffect } from 'react'
import * as d3 from 'd3'

export default function Chart({ data = [] }){
  const ref = useRef(null)

  useEffect(() => {
    const el = ref.current
    if (!el) return

    const width = el.clientWidth
    const height = 400
    d3.select(el).selectAll('*').remove()

    const svg = d3.select(el)
      .append('svg')
      .attr('width', width)
      .attr('height', height)

    const parsed = (data || []).map((d, i) => ({
      x: i,
      y: typeof d.price === 'number' ? d.price : (Number(d) || Math.random()*100)
    }))

    const x = d3.scaleLinear().domain([0, Math.max(1, parsed.length-1)]).range([40, width-20])
    const y = d3.scaleLinear().domain([d3.min(parsed, d=>d.y) ?? 0, d3.max(parsed,d=>d.y) ?? 100]).nice().range([height-30, 10])

    const line = d3.line().x(d=>x(d.x)).y(d=>y(d.y)).curve(d3.curveMonotoneX)

    svg.append('path').datum(parsed).attr('fill','none').attr('stroke','#0ea5e9').attr('stroke-width',2).attr('d', line)

    // Axes
    const xAxis = d3.axisBottom(x).ticks(6)
    const yAxis = d3.axisLeft(y).ticks(6)

    svg.append('g').attr('transform', `translate(0,${height-30})`).call(xAxis)
    svg.append('g').attr('transform', `translate(40,0)`).call(yAxis)

  }, [data])

  return (
    <div ref={ref} style={{width: '100%'}} className="h-96" />
  )
}
