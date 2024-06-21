puts ">>> Ruby / rendering covers..."

require "json"
require "wkhtmltoimage-binary"


def render_cover(issueIndex:, titleText:, releaseDate:)
  puts "        / rendering issue#{issueIndex} cover..."

  content = File.read "./covers/core.html"
  processed = content % {
    issueIndex:,
    titleText:,
    releaseDate:,
  }

  kit = IMGKit.new(processed)
  kit.to_file("./assets/covers/#{index}.png")

  return export
end


source = File.read("./site/src/issues-config.json")

issues = JSON.parse(source)

issues.each do |issue|
  render_cover(
    issueIndex: issue["issueIndex"],
    titleText: issue["title"],
    releaseDate: issue["date"]
  )
end
